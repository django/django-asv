from ...utils import bench_setup
import sys
import os
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.conf import settings

def make_request():
    environ = {
        'PATH_INFO': '/',
        'QUERY_STRING': '',
        'REQUEST_METHOD': 'GET',
        'SCRIPT_NAME': '',
        'SERVER_NAME': 'testserver',
        'SERVER_PORT': 80,
        'SERVER_PROTOCOL': 'HTTP/1.1',
        "wsgi.input": sys.stdin
    }

    return WSGIRequest(environ)

class L10nRender:

    def setup(self):
        bench_setup()
        settings.USE_I18N = False
        settings.USE_L10N = True
        settings.TEMPLATE_DIRS = (
        os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')))
        settings.INSTALLED_APPS = ['l10n_render', 'django.contrib.auth', 'django.contrib.contenttypes']
        settings.TEMPLATES = TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                    os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')),
                ],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.contrib.auth.context_processors.auth',
                        'django.template.context_processors.debug',
                        'django.template.context_processors.i18n',
                        'django.template.context_processors.media',
                        'django.template.context_processors.static',
                        'django.template.context_processors.tz',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]
        self.req_object = make_request()
    
    def time_render(self):
        context = {'numbers': range(0, 200)}
        render(self.req_object, 'list.html', context)
