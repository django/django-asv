from django.http import HttpRequest
from django.shortcuts import render

from django import VERSION, template

from ...utils import bench_setup


class TemplateRender:
    def setup(self):
        bench_setup()
        self.context = {
            "objects1": [object(), object(), object(), object(), object()],
            "objects2": [object(), object(), object(), object(), object()],
            "object1": object(),
            "object2": object(),
            "object3": None,
            "num1": 1,
            "num2": 2,
            "boolean1": True,
            "SCRIPT_CONTENT_URL": "/some/prefix",
            "WEBSITE_DOMAIN": "http://www.somedomain.com",
            "SHOW_ALT_HEADER": "True",
            "base_template": "base.html",
        }

    def time_template_render(self):
        if VERSION >= (4, 0):
            render(HttpRequest(), "permalink.html", self.context)
        else:
            render(HttpRequest(), "permalink_django_lte_40.html", self.context)

    def time_render_simple(self):
        context = template.Context({"stuff": "something"})
        t = template.Template("{{ stuff }}")
        for i in range(10):
            t.render(context)
            t.render(context)
            t.render(context)
            t.render(context)
            t.render(context)
            t.render(context)
            t.render(context)
            t.render(context)
            t.render(context)
            t.render(context)
