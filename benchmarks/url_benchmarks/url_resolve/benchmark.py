from django.urls import resolve

from ...utils import bench_setup


class UrlResolve:
    def setup(self):
        bench_setup()

    def time_resolve(self):
        for i in range(100):
            resolve("/basic/")
            resolve("/fallthroughview/")
            resolve("/replace/1")
