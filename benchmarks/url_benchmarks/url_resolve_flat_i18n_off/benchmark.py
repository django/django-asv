from ...utils import bench_setup
from django.urls import Resolver404, resolve
from django.conf import settings

class UrlResolve:

    def setup(self):
        bench_setup()
        settings.ROOT_URL_CONF = "url_resolve_flat_i18n_off.urls"
        settings.USE_I8N = False
    
    def teardown(self):
        settings.ROOT_URL_CONF = "benchmarks.urls"
        settings.USE_I8N = True
    
    def time_i8n_off(self):
        paths = (
        '/user/repo/feature19',
        '/section0/feature0',
        '/en/feature10',
        '/ru/feature10',
        '/missing',
        )
        for i in range(0, 100):
            for path in paths:
                try:
                    resolve(path)
                except Resolver404:
                    pass
