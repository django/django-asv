from django.urls import Resolver404, resolve

from ...utils import bench_setup


class UrlResolveFlat:
    def setup(self):
        bench_setup()

    def time_resolve_flat(self):
        paths = (
            "/user/repo/feature19",
            "/section0/feature0",
            "/en/feature10",
            "/ru/feature10",
            "/missing",
        )
        for i in range(100):
            for path in paths:
                try:
                    resolve(path)
                except Resolver404:
                    pass
