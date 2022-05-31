import os

import django
from django import VERSION, template
from django.http import HttpRequest
from django.shortcuts import render

try:
    os.environ["DJANGO_SETTINGS_MODULE"] = "benchmarks.settings"
    django.setup()
except RuntimeError:
    pass


objects1 = [object(), object(), object(), object(), object()]
objects2 = [object(), object(), object(), object(), object()]
object1 = object()
object2 = object()
object3 = None
num1 = 1
num2 = 2
boolean1 = True
SCRIPT_CONTENT_URL = "/some/prefix"
WEBSITE_DOMAIN = "http://www.somedomain.com"
SHOW_ALT_HEADER = "True"


class TemplateBenchmarks:
    def setup(self):
        self.context = {
            "objects1": objects1,
            "objects2": objects2,
            "object1": object1,
            "object2": object2,
            "object3": object3,
            "num1": num1,
            "num2": num2,
            "boolean1": boolean1,
            "SCRIPT_CONTENT_URL": SCRIPT_CONTENT_URL,
            "WEBSITE_DOMAIN": WEBSITE_DOMAIN,
            "SHOW_ALT_HEADER": SHOW_ALT_HEADER,
            "base_template": "base.html",
        }

    def time_template_render(self):
        if VERSION >= (4, 0):
            render(HttpRequest(), "permalink.html", self.context)
        else:
            render(HttpRequest(), "permalink_django_lte_40.html", self.context)

    def time_template_render_simple(self):
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

    def time_template_compilation(self):
        # Just compile the template, no rendering
        template.Template(
            """
            {% for v in vals %}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
            {% endfor %}
        """
        )
