from django.urls import resolve

from ...utils import bench_setup


class UrlResolveNested:
    def setup(self):
        bench_setup()

    def time_resolve_nested(self):
        resolve("/0/00/000/0000/00000/000000/0000000/00000000/leaf")
