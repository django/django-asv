from django import template

from ...utils import bench_setup


class TemplateCompile:
    def setup(self):
        bench_setup()

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
