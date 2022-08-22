from django.urls import reverse

from ...utils import bench_setup


class UrlReverse:
    def setup(self):
        bench_setup()

    def time_reverse(self):
        reverse("url_reverse:basic")
        reverse("url_reverse:catchall")
        reverse("url_reverse:vars", args=[1])
        reverse("url_reverse:vars", kwargs={"var": 1})
