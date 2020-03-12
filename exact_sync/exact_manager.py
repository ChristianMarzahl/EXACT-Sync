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

    def json_post_request(self,url) -> dict:
        req = requests.post(url, auth = (self.username, self.password))
        if req.status_code==403:
            raise AccessViolationError('Permission denied by exact server for current user'+req.text)
        try: 
            return json.loads(req.text)
        except:
            return dict()

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
        status, obj = self.get('images/api/list_imagesets/')
        if (status != 200):
            raise ExactProcessError('Unable to retrieve list of image sets')
        return json.loads(obj)

    def retrieve_annotations(self,image_id:int) -> list:
        obj = self.json_get_request(self.serverurl+'annotations/api/annotation/load/?image_id=%d' % image_id)
        self.log(0, 'Retrieving annotations from ', image_id)
        if 'annotations' in obj:
            return obj['annotations']
        else:
            return []


    def update_annotation(self, annotation_id:int,  image_id:int, annotationtype_id:int, vector:list, last_modified:int, blurred:bool=False, guid:str='', deleted:int=0, description:str=''):
        data = {
            'annotation_id': annotation_id,
            'image_id' : image_id,
            'annotation_type_id' : annotationtype_id,
            'vector' : list_to_exactvector(vector),
            'unique_identifier' : guid,
            'deleted' : deleted,
            'last_edit_time' : datetime.datetime.fromtimestamp(last_modified).strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'blurred' : blurred,
            'description' : description
        }
        self.log(1, f'Update of remote annotation {guid}, ts={data["last_edit_time"]}')
        status, ret = self.post('annotations/api/annotation/update/', data=json.dumps(data), headers={'content-type':'application/json'})
        if status==200:
            return ret
        else: 
            self.log(10,'Unable to update annotation, message was: '+ret)
            raise ExactProcessError('Unable to update annotation')

    def create_annotation(self, image_id:int, annotationtype_id:int, vector:list, last_modified:int, blurred:bool=False, guid:str='', description:str='', deleted:bool=False):
        data = {
            'image_id': image_id,
            'annotation_type_id' : annotationtype_id,
            'vector' : list_to_exactvector(vector),
            'unique_identifier' : guid,
            'deleted' : deleted,
            'last_edit_time' : datetime.datetime.fromtimestamp(last_modified).strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'blurred' : blurred,
            'description' : description
        }
        self.log(1,f'Creating remote annotation {guid} with ts = {data["last_edit_time"]}')
        status, ret = self.post('annotations/api/annotation/create/', data=json.dumps(data), headers={'content-type':'application/json'})
        if status==201:
            return ret
        else: 
            self.log(10,'Unable to create annotation, message was: '+ret)
            raise ExactProcessError('Unable to create annotation')

    def retrieve_imagelist(self, imageset_id:int) -> list:
        # this is really a format fuckup. But let's parse it nevertheless...
        self.log(0, 'Retrieving image list for ',imageset_id)
        il = self.csv_get_request(self.serverurl+'images/imagelist/%d/' % imageset_id)
        return ExactImageList([[int(x.split('?')[0].split('/')[-2]),x.split('?')[1]] for x in il if '?' in x])

    def retrieve_imageset(self,imageset_id):
        return self.json_get_request(self.serverurl+'images/api/imageset/load?image_set_id=%d' % imageset_id)['image_set']

    def get(self, url):
        ret= requests.get(self.serverurl+url, auth=(self.username, self.password))
        return ret.status_code, ret.text

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

    def create_progressbar(self, e:encoder.MultipartEncoder):

        bar = tqdm(total=100)
        def upload_monitor(monitor:encoder.MultipartEncoderMonitor):
            bar.update((float(monitor.bytes_read)/monitor.len) * 100)
        return upload_monitor

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

    def post(self, url, data, files=None, **kwargs):
        try:
            ret= requests.post(self.serverurl+url, auth=(self.username, self.password), data=data, files=files, **kwargs)
        except requests.exceptions.ConnectionError as e:
            return self.post(url, data, files, **kwargs)
        try:
            return ret.status_code, json.loads(ret.text)
        except:
            return ret.status_code, ret.text
    
    def get(self, url):
        ret= requests.get(self.serverurl+url, auth=(self.username, self.password))
        return ret.status_code, ret.text

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