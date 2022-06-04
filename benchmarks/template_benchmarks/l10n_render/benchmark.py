import os
import sys

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from ...utils import bench_setup


def make_request():
    environ = {
        "PATH_INFO": "/",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "GET",
        "SCRIPT_NAME": "",
        "SERVER_NAME": "testserver",
        "SERVER_PORT": 80,
        "SERVER_PROTOCOL": "HTTP/1.1",
        "wsgi.input": sys.stdin,
    }

    return WSGIRequest(environ)


class L10nRender:
    def setup(self):
        bench_setup()
        settings.USE_I18N = False
        settings.USE_L10N = True
        settings.INSTALLED_APPS = [
            "l10n_render",
            "django.contrib.auth",
            "django.contrib.contenttypes",
        ]
        self.req_object = make_request()

    def time_render(self):
        context = {"numbers": range(0, 200)}
        render(self.req_object, "list.html", context)
