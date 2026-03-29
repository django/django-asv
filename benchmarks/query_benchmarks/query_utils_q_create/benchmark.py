from django.db.models import Q

from ...utils import bench_setup
from .models import Content


class QueryQCreate:
    def setup(self):
        bench_setup(migrate=True)
        Content.objects.bulk_create(
            [Content(a=i, b=i % 5, c=f"val-{i}") for i in range(1000)]
        )
        self.connector_OR = Q.OR

    def teardown(self):
        Content.objects.all().delete()

    def time_q_create(self):
        content_list = list(Content.objects.all())
        Q.create(content_list, self.connector_OR)

    def time_q_create_nested_loop(self):
        content_list = [
            Q.create(
                [(content.a, content.b, content.c) for content in Content.objects.all()]
            )
        ]
        Q.create(content_list, self.connector_OR)
