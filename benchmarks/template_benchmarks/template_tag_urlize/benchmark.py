from django.template.defaultfilters import urlize

from ...utils import bench_setup


class Urlize:
    def setup(self):
        bench_setup()

    def time_urlize(self):
        urlize("Django. " * 100)
        urlize("https://www.djangoproject.com/ " * 100)
