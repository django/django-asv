from django.test import Client

from ...utils import bench_setup


class HttpMethods:
    def setup(self):
        bench_setup()
        self.client = Client()

    def time_get_method(self):
        self.client.get("http-methods/get")
        self.client.get("http-methods/get")
        self.client.get("http-methods/get")
        self.client.get("http-methods/get")
        self.client.get("http-methods/get")

    def time_post_method(self):
        self.client.post("http-methods/post")
        self.client.post("http-methods/post")
        self.client.post("http-methods/post")
        self.client.post("http-methods/post")
        self.client.post("http-methods/post")
