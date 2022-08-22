from django.urls import Resolver404, resolve

from ...utils import bench_setup


class UrlResolveFlat:
    def setup(self):
        bench_setup()

    def time_resolve_flat(self):
        paths = (
            "/url-resolve-flat/user/repo/feature19",
            "/url-resolve-flat/section0/feature0",
            "/url-resolve-flat/en/feature10",
            "/url-resolve-flat/ru/feature10",
            "/url-resolve-flat/missing",
        )
        for i in range(100):
            for path in paths:
                try:
                    resolve(path)
                except Resolver404:
                    pass
