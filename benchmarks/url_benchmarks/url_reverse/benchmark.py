from django.urls import reverse

from ...utils import bench_setup


class UrlReverse:
    def setup(self):
        bench_setup()

    def time_reverse(self):
        reverse("basic")
        reverse("catchall")
        reverse("vars", args=[1])
        reverse("vars", kwargs={"var": 1})
