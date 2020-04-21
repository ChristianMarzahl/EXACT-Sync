from pathlib import Path
import os
import requests
import json
from requests.auth import HTTPBasicAuth
import time
import datetime
import re
import sys
from functools import partial
import threading
import queue
from tqdm import tqdm
from requests_toolbelt.multipart import encoder

from exact_sync.exact_enums import *
from exact_sync.exact_errors import *

class ExactImageList():
    def __init__(self, imagelist:list):
        self._list = imagelist
        if len(imagelist)>0:
            if len(imagelist[0])!=2:
                raise ValueError('Must be a list of lists of size 2.')
    
    @property
    def list(self) -> list:
        return self._list

    def dict(self) -> dict:
        return {x:y for x,y in self._list}


class ExactManager():

    def __init__(self, username:str=None, password:str=None, serverurl:str=None, logfile=sys.stdout, loglevel:int=1, statusqueue:queue.Queue=None):
        self.username = username
        self.password = password
        self.serverurl = serverurl if serverurl[-1]=='/' else serverurl+'/'
        self.statusqueue = statusqueue
        self.progress_denominator = 1
        self.progress_offset = 0
        self.set_progress_properties(1,0)
        self.multi_threaded=True
        self.num_threads=10
        if (self.multi_threaded):
            self.jobqueue = queue.Queue()
            self.resultQueue = queue.Queue()
            self.workers={}
            for k in range(self.num_threads):
                self.workers[k] = threading.Thread(target=self.queueWorker, daemon=True)
                self.workers[k].start()

        self.logfile = logfile
        self.loglevel = loglevel
        self.log(0,f'Created EXM with username {username}, serverurl: {serverurl}')        
        stat, ret = self.get('timesync/')
        timeoffset = abs(json.loads(ret)['unixtime']-time.time())
        if (stat==200) and (timeoffset>10):
            raise ExactProcessError('Your computer''s clock is incorrect')
        else:
            self.log(1,f'Time offset to server is: {timeoffset} seconds.')

    #region helper functions

    def log(self,level, *args):
        logmsg=' '.join([str(x) for x in args])
        if level>=self.loglevel:
            self.logfile.write( '%s ' % str(datetime.datetime.now()) + logmsg +'\n')
        if (self.statusqueue is not None) and (level>1):
            self.statusqueue.put((1, logmsg))

    def progress(self, value:float, callback:callable=None):
        value=value/self.progress_denominator+self.offset
        if (self.statusqueue is not None):
            self.statusqueue.put((0, value*100 if value<1 else -1))
        if (callback is not None):
            callback(value*100)

    def set_progress_properties(self, denominator:float, offset:float):
        self.progress_denominator=float(denominator)
        self.offset=float(offset)

    def queueWorker(self):
        while (True):
            status, newjob, context = self.jobqueue.get()
            if (status==-1):
#                print('Stopping worker')
                break
            ret = newjob()
            self.resultQueue.put((ret, context))

    def terminate(self):
        for k in range(self.num_threads):
            self.jobqueue.put((-1,0,0))

    def create_progressbar(self, e:encoder.MultipartEncoder):

        bar = tqdm(total=100)
        def upload_monitor(monitor:encoder.MultipartEncoderMonitor):
            bar.update((float(monitor.bytes_read)/monitor.len) * 100)
        return upload_monitor

    def get_filename_from_cd(self, cd):
        """
        Get filename from content-disposition
        """
        if not cd:
            return None
        fname = re.findall('filename=(.+)', cd)
        if len(fname) == 0:
            return None
        return fname[0]

    @staticmethod
    def list_to_exactvector(vector):
        retdict = {f'x{(i+1)}': v[0] for i, v in enumerate(vector)}
        retdict.update({f'y{i+1}': v[1] for i, v in enumerate(vector)} )
        return retdict
    #endregion

    #region POST commands

    def json_post_request(self,url) -> dict:
        req = requests.post(url, auth = (self.username, self.password))
        if req.status_code==403:
            raise AccessViolationError('Permission denied by exact server for current user'+req.text)
        try: 
            return json.loads(req.text)
        except:
            return dict()


    def update_annotation_from_dict(self, annotation:dict): 

        annotation_id = annotation['id']
        image_id = annotation['image']['id']
        annotationtype_id = annotation['annotation_type']['id']
        vector = annotation['vector']
        last_modified = annotation.get('last_edit_time', None)
        blurred =annotation.get('blurred', False)
        guid = annotation.get('unique_identifier', '')
        deleted = annotation.get('deleted', False)
        description = annotation.get('description', '')
        meta_data = annotation.get('meta_data', None)

        self.update_annotation(annotation_id,  image_id, annotationtype_id, vector, last_modified, blurred, guid, deleted, description, meta_data)
    

    def update_annotation(self, annotation_id:int,  image_id:int, annotationtype_id:int, vector:list, last_modified:int=None, blurred:bool=False, guid:str=None, deleted:int=0, description:str='', meta_data:dict=None):
        data = {
            'annotation_id': annotation_id,
            'image_id' : image_id,
            'annotation_type_id' : annotationtype_id,
            'vector' : vector if isinstance(vector, dict) else ExactManager.list_to_exactvector(vector),
            'deleted' : deleted,
            'blurred' : blurred,
            'description' : description,
            'meta_data': meta_data
        }

        if guid is not None:
            data['unique_identifier'] = guid

        if last_modified != None:
            data['last_edit_time'] = datetime.datetime.fromtimestamp(last_modified).strftime('%Y-%m-%dT%H:%M:%S.%f') if isinstance(last_modified, int) else last_modified

        self.log(1, f'Update of remote annotation {guid}')
        status, ret = self.post('annotations/api/annotation/update/', data=json.dumps(data), headers={'content-type':'application/json'})
        if status==200:
            return ret
        else: 
            self.log(10,'Unable to update annotation, message was: '+ret)
            raise ExactProcessError('Unable to update annotation')

    def create_annotation(self, image_id:int, annotationtype_id:int, vector:list, last_modified:int=None, blurred:bool=False, guid:str=None, description:str='', deleted:bool=False, meta_data:dict=None):
        data = {
            'image_id': image_id,
            'annotation_type_id' : annotationtype_id,
            'vector' : vector if isinstance(vector, dict) else ExactManager.list_to_exactvector(vector),
            'deleted' : deleted,
            'blurred' : blurred,
            'description' : description,
            'meta_data': meta_data
        }

        if guid is not None:
            data['unique_identifier'] = guid

        if last_modified != None:
            data['last_edit_time'] = datetime.datetime.fromtimestamp(last_modified).strftime('%Y-%m-%dT%H:%M:%S.%f')

        self.log(1,f'Creating remote annotation {guid}')
        status, ret = self.post('annotations/api/annotation/create/', data=json.dumps(data), headers={'content-type':'application/json'})
        if status==201:
            return ret
        else: 
            self.log(10,'Unable to create annotation, message was: '+ret)
            raise ExactProcessError('Unable to create annotation')

    def upload_image_to_imageset(self, imageset_id:int, filename:str) -> bool:
        e = encoder.MultipartEncoder(fields={'files[]': (os.path.basename(filename), open(filename, 'rb'), 'application/octet-stream')})
        p_bar = self.create_progressbar(e)
        m = encoder.MultipartEncoderMonitor(e, p_bar)
        headers = {'Content-Type': m.content_type, 'referer': self.serverurl}
        self.log(1, 'Uploading image',filename,'to',imageset_id)
        status, obj = self.post('images/image/upload/%d/'%imageset_id, data=m, headers=headers, timeout=120)
        if (status==200):
            return obj
        else:
            raise ExactProcessError('Unable to upload, response is: '+str(obj))

    def add_product_to_imageset(self, product_id:int, imageset_id:int):
        """[Assign a product to an image set]
        
        Arguments:
            product_id {int} -- [Product Id
            imageset_id {int} -- [Imageset ID]
        
        Returns:
            [type] -- [description]
        """
        data = {'image_set_id':imageset_id,
                'product_id':product_id}

        self.log(1, 'Adding product',product_id,'to',imageset_id)
        obj = self.post('images/api/imageset/product/add/',data=data )       
        return obj

    def create_product(self, name:str, team:dict, description:str=None):
        """Create a new team product
        
        Arguments:
            name {str} -- Product name
            team {dict} -- Team {'id': 123}
        
        Keyword Arguments:
            description {str} -- [description] (default: {None})
        """
        data = {'name':name,
                'team':team,
                'description': description}

        obj = self.post('administration/api/products/create/',data=data )       
        return obj

    def create_imageset(self, name:str, team:dict, description:str=None, location:str=None, 
                            public:bool=False, public_collaboration:bool=False, image_lock:bool=False,
                            priority:int=0, main_annotation_type:dict=None, collaboration_type:int=0, products:[dict]=None):
        """Create a new ImageSet and assign a team
        
        Arguments:
            name {str} -- Imageset name
            team {dict} -- Dict with team id {'id': 123}
        
        Keyword Arguments:
            description {str} -- [description] (default: {None})
            location {str} -- [description] (default: {None})
            public {bool} -- [description] (default: {False})
            public_collaboration {bool} -- [description] (default: {False})
            image_lock {bool} -- [description] (default: {False})
            priority {int} -- [description] (default: {0})
            main_annotation_type {dict} -- Dict with Id (default: {None})
            collaboration_type {int} -- [description] (default: {0})
            products {[type]} -- [List of porudcts [{'id':123}]] (default: {None})
        
        Raises:
            AssertionError: [description]
        
        Returns:
            [type] -- [description]
        """

        if 'id' not in team:
            raise AssertionError("Team has to contain id")
        
        data = {'name':name,
                'team':team,
                'location': location,
                'description': description,
                'public': public,
                'public_collaboration': public_collaboration,
                'image_lock': image_lock,
                'priority': priority,
                'main_annotation_type': main_annotation_type,
                'collaboration_type': collaboration_type,
                'products': products}

        obj = self.post('images/api/imageset/create/',data=data )       
        return obj


    def create_annotationtype(self,product_id:int, name:str, vector_type:int, color_code:str='#FF0000',
                              area_hit_test:bool=True, closed:bool=False, default_width:int=50,
                              default_height:int=50, sort_order:int=0
                              ):
        """Create ne new AnnotationType
        
        Arguments:
            product_id {int} -- Product Id
            name {str} -- Annotation Name
            vector_type {int} -- BOUNDING_BOX = 1; POINT = 2; LINE = 3; MULTI_LINE = 4; 
                                POLYGON = 5; FIXED_SIZE_BOUNDING_BOX = 6; GLOBAL = 7
        
        Keyword Arguments:
            color_code {str} -- [description] (default: {'#FF0000'})
            area_hit_test {bool} -- [description] (default: {True})
            closed {bool} -- [description] (default: {False})
            default_width {int} -- [description] (default: {50})
            default_height {int} -- [description] (default: {50})
            sort_order {int} -- [description] (default: {0})
        
        Raises:
            ExactProcessError: [description]
        
        Returns:
            [type] -- [description]
        """                   
        data = {'product_id': product_id,
                'name': name[0:20],
                'color_code': color_code,
                'sort_order':sort_order,
                'vector_type': vector_type,
                'default_width': default_width,
                'default_height': default_height,
                'area_hit_test':area_hit_test,
                'closed':closed}
        self.log(1,'Creating remote annotation type: ',name,'product',product_id,'vector type',vector_type)
        
        status, ret =  self.post('administration/api/annotation_type/create/', data=data)
        if (status==201):
            return ret
        else:
            self.log(10,'Unable to create annotation, message was: '+ret)
            raise ExactProcessError('Unable to create annotation')

    def upload_annotation_mediafile(self, annotation_id:int, filename:str, media_file_type:int) -> bool:
        """Attach a media file to an annotations
        
        Arguments:
            annotation_id {int} -- Annotation ID
            filename {str} -- File Path
            media_file_type {int} -- 1 Undefined, 2 Image, 3 Video, 4 Audio
        
        Raises:
            ExactProcessError: Unable to upload media file
        
        Returns:
            [object] -- List of uploaded media files
        """
        e = encoder.MultipartEncoder(fields={'files[]': (os.path.basename(filename), open(filename, 'rb'), 'application/octet-stream')})
        p_bar = self.create_progressbar(e)
        m = encoder.MultipartEncoderMonitor(e, p_bar)
        headers = {'Content-Type': m.content_type, 'referer': self.serverurl}
        self.log(1, 'Uploading media file',filename,'to',annotation_id)
        status, obj = self.post('annotations/api/annotation/mediafile/upload/{0}/{1}/'.format(annotation_id,media_file_type), data=m, headers=headers, timeout=120)
        if (status==200):
            return obj
        else:
            raise ExactProcessError('Unable to upload, response is: '+str(obj))

    def post(self, url, data, files=None, **kwargs):
        try:
            ret= requests.post(self.serverurl+url, auth=(self.username, self.password), data=data, files=files, **kwargs)
        except requests.exceptions.ConnectionError as e:
            return self.post(url, data, files, **kwargs)
        try:
            return ret.status_code, json.loads(ret.text)
        except:
            return ret.status_code, ret.text

    #endregion

    
    #region GET commands

    def get(self, url, params={}):
        ret= requests.get(self.serverurl+url, auth=(self.username, self.password), params=params)
        return ret.status_code, ret.text

    def json_get_request(self,url) -> dict:
        req = requests.get(url, auth = (self.username, self.password))
        if req.status_code==403:
            raise AccessViolationError('Permission denied by exact server for current user'+req.text)
        try: 
            return json.loads(req.text)
        except:
            return dict()

    def csv_get_request(self,url) -> list:
        req = requests.get(url, auth = (self.username, self.password))
        try: 
            return req.text.split(',')
        except:
            return []

    def retrieve_annotationtypes(self, imageset_id:int) -> list:
        obj = self.json_get_request(self.serverurl+'annotations/api/annotation/loadannotationtypes/?imageset_id=%d' % imageset_id)['annotation_types']        
        return obj

    def download_image(self, image_id:int, target_path: Path, callback:callable, original_image:bool=False):
        status,filename = self.getfile('images/api/image/download/{0}/?original_image={1}'.format(image_id, original_image), target_path, callback=callback)
        self.log(1, 'Downloading image',image_id,'to', target_path)
        return filename

    def retrieve_imagesets(self):
        """List of all image sets
        
        Raises:
            ExactProcessError: 'Unable to retrieve list of image sets
        
        Returns:
            [type] -- List of images sets with images and products
        """
        status, obj = self.get('images/api/list_imagesets/')
        if (status != 200):
            raise ExactProcessError('Unable to retrieve list of image sets')
        return json.loads(obj)

    def retrieve_annotations(self,image_id:int) -> list:
        """Download image annotations 
        
        Arguments:
            image_id {int} -- Image Id
        
        Returns:
            list -- List of Annotations
        """
        obj = self.json_get_request(self.serverurl+'annotations/api/annotation/load/?image_id=%d' % image_id)
        self.log(0, 'Retrieving annotations from ', image_id)
        if 'annotations' in obj:
            return obj['annotations']
        else:
            return []

    def retrieve_imageset(self,imageset_id):
        return self.json_get_request(self.serverurl+'images/api/imageset/load?image_set_id=%d' % imageset_id)['image_set']
   
    def getfile(self, url, target_path, callback) -> (int, str, bytes):
        with requests.get(self.serverurl+url, auth=(self.username, self.password), stream=True) as r:
            r.raise_for_status()
            f = open(str(target_path),'wb')
            siz=0
            chunk_size=8192
            for chunk in tqdm(r.iter_content(chunk_size), total=int(r.headers['content-length']) / chunk_size, desc=target_path.name): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    siz += len(chunk)
                    prog=float(siz)/int(r.headers['content-length'])
                    self.progress(prog, callback=callback)
            f.close()
        return r.status_code, target_path

    def filter_products(self, name:str=None, id:int=-1, team:dict=None):
        """Filter products
        
        Keyword Arguments:
            name {str} -- Product name (default: {None})
            id {int} -- Product id (default: {-1})
            team {dict} -- Team {'id': 123} (default: {None})
        
        Returns:
            [type] -- [description]
        """
        params = {'name':name,
                'team':team,
                'id': id}

        obj = self.get('administration/api/products/filter/', params=params)       
        return obj

    def filter_teams(self, name:str=None, id:int=-1):
        """Filter teams
        
        Keyword Arguments:
            name {str} -- Team name (default: {None})
            id {int} -- Team id (default: {-1})
        
        Returns:
            [type] -- [description]
        """
        params = {'name':name,
                'id': id}

        obj = self.get('users/api/team/filter/', params=params)       
        return obj

    #endregion

    #region DELETE

    def delete_annotationtype(self, annotation_type_id:int):
        """Delete the annotation type
        
        Arguments:
            annotation_type_id {int} -- Annotation Type
        
        Returns:
            [type] -- [description]
        """
        data = {'annotation_type_id':annotation_type_id}
        return self.post('administration/api/annotation_type/delete/', data=data)

    #endregion
