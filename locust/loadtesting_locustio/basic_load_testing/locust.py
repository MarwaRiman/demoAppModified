import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5) # it waits 1 to 5 seconds between visiting 2 different endpoints 

    @task
    def index_page(self):
        self.client.get(url="/hello")

    @task
    def slow_page(self):
        self.client.get(url="/slow")
