import os
os.environ["GEVENT_SUPPORT"] = "1"

import random
import json
from locust import HttpUser, between, task
from locust_plugins import run_single_user

class ApiUser(HttpUser):
    #wait_time = between(5, 15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.username = '*****'
        self.password = '****'
        self.max_level = 10
        self.image_ids = [335]
    
    def on_start(self):
        # login user
        response = self.client.get('/accounts/login/')
        self.csrftoken = response.cookies['csrftoken']

        headers={'X-CSRFToken': self.csrftoken, "referer": self.host} if "https" in self.host else {'X-CSRFToken': self.csrftoken}
        result = self.client.post('/accounts/login/',
                         {'username': self.username, 'password': self.password}, 
                         headers=headers)

        # select random image
        self.image_id = random.choice(self.image_ids)

        # get image information
        response = self.client.get(f'/api/v1/images/images/{self.image_id}/slide_information/', headers={'X-CSRFToken': self.csrftoken}) 
        self.slide_information = json.loads(response.text)

    #@task
    def index(self):
        result = self.client.get(f"/annotations/{self.image_id}/", headers={'X-CSRFToken': self.csrftoken})
        
    @task
    def get_tile(self):
        level = random.randint(0, min(self.max_level, len(self.slide_information["level_tiles"]) - 1))
        num_x_tiles, num_y_tiles = self.slide_information["level_tiles"][level]
        x_tile = random.randint(0, num_x_tiles -1)
        y_tile = random.randint(0, num_y_tiles -1)
        result = self.client.get(f"/images/image/{self.image_id}/1/1/tile_files/{level}/{x_tile}_{y_tile}.jpeg", 
                                    headers={'X-CSRFToken': self.csrftoken})

if __name__ == "__main__":
    ApiUser.host = "http://127.0.0.1:8000" #"https://exact.cs.fau.de"
    run_single_user(ApiUser, include_time=True, include_length=True)