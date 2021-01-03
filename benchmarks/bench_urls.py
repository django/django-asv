import os

import django
from django.urls import Resolver404, resolve, reverse

try:
    os.environ["DJANGO_SETTINGS_MODULE"] = "benchmarks.settings"
    django.setup()
except RuntimeError:
    pass


class URLBenchmarks:
    def setup(self):
        pass

    def teardown(self):
        pass

    def time_url_resolve(self):
        for i in range(0, 100):
            resolve("/basic/")
            resolve("/fallthroughview/")
            resolve("/replace/1")

    def time_url_resolve_flat(self):
        paths = (
            "/user/repo/feature19",
            "/section0/feature0",
            "/en/feature10",
            "/ru/feature10",
            "/missing",
        )
        for i in range(0, 100):
            for path in paths:
                try:
                    resolve(path)
                except Resolver404:
                    pass

    def time_url_resolve_nested(self):
        resolve("/0/00/000/0000/00000/000000/0000000/00000000/leaf")

    def time_url_reverse(self):
        reverse("basic")
        reverse("catchall")
        reverse("vars", args=[1])
        reverse("vars", kwargs={"var": 1})
        # repeat for more stable benchmark
        reverse("basic")
        reverse("catchall")
        reverse("vars", args=[1])
        reverse("vars", kwargs={"var": 1})
