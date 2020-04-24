from time import sleep
import re

class PaginationBaseAPI(object):
    
    def _get_all(self, func:callable, **kwargs):

        data = func(**kwargs)

        if kwargs.get('async_req'):
            data = data.get()
        if data.next != None:   
            threads = []             
            limit = int(re.findall("limit=([0-9]*)", data.next)[0])
            offset = int(re.findall("offset=([0-9]*)", data.next)[0])
            for page_offset in range(offset, data.count, offset):
                kwargs['offset'] = page_offset
                if kwargs.get('async_req'):
                    thread = func(**kwargs)
                    threads.append(thread)
                else:    
                    (new_data) = func(**kwargs)
                    data.results += new_data.results

            if kwargs.get('async_req'):
                while (len(threads) > 0):
                    for thread in threads:
                        if thread.ready():
                            data.results += thread.get().results
                            threads.remove(thread)
                    sleep(0.25)

            data.next = None
            data.previous = None
        return data

