from django.db.models import Count

from ...utils import bench_setup
from .models import Book


class QueryAggr:
    def setup(self):
        bench_setup(migrate=True)

    def time_aggregate(self):
        Book.objects.all().aggregate(Count("title"))
        Book.objects.all().aggregate(Count("title"))
        Book.objects.all().aggregate(Count("title"))

        Book.objects.all().aggregate(Count("id"))
        Book.objects.all().aggregate(Count("id"))
        Book.objects.all().aggregate(Count("id"))
