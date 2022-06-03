from django import template

from ...utils import bench_setup

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


class TemplateCompile:
    def setup(self):
        bench_setup()
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

    def time_template_compile(self):
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
