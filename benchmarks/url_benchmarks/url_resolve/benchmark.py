from django.urls import resolve

from ...utils import bench_setup


class UrlResolve:
    def setup(self):
        bench_setup()

    def time_resolve(self):
        for i in range(100):
            resolve("/url-resolve/basic/")
            resolve("/url-resolve/fallthroughview/")
            resolve("/url-resolve/replace/1")

    def time_resolve_path(self):
        resolve("/url-resolve/num/1/")

    def time_resolve_literal_path(self):
        resolve("/url-resolve/basic-path/")
