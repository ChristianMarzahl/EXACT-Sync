import os
os.environ["GEVENT_SUPPORT"] = "1"

import random
import json
from locust import HttpUser, between, task
#from locust_plugins import run_single_user

image_ids = [329, 331, 324]

username = 'exact'
password = 'exact'


class ApiUser(HttpUser):
    #wait_time = between(5, 15)
    
    def on_start(self):
        # login user
        response = self.client.get('/accounts/login/')
        self.csrftoken = response.cookies['csrftoken']
        self.client.post('/accounts/login/',
                         {'username': username, 'password': password}, 
                         headers={'X-CSRFToken': self.csrftoken})

        # select random image
        self.image_id = random.choice(image_ids)

        # get image information
        response = self.client.get(f'/api/v1/images/images/{self.image_id}/slide_information/', headers={'X-CSRFToken': self.csrftoken}) 
        self.slide_information = json.loads(response.text)

    #@task
    def index(self):
        result = self.client.get(f"/annotations/{self.image_id}/", headers={'X-CSRFToken': self.csrftoken})
        
    @task
    def get_tile(self):
        level = random.randint(0, len(self.slide_information["level_tiles"]) - 1)
        num_x_tiles, num_y_tiles = self.slide_information["level_tiles"][level]
        x_tile = random.randint(0, num_x_tiles -1)
        y_tile = random.randint(0, num_y_tiles -1)
        result = self.client.get(f"/images/image/{self.image_id}/1/1/tile_files/{level}/{x_tile}_{y_tile}.jpeg", 
                                    headers={'X-CSRFToken': self.csrftoken})

#if __name__ == "__main__":
#    ApiUser.host = "http://127.0.0.1:1337"
#    run_single_user(ApiUser, include_time=True, include_length=True)