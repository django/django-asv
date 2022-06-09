from ...utils import bench_setup
from .models import Book


class QueryExclude:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_exclude(self):
        list(Book.objects.exclude(id=1))
        list(Book.objects.exclude(id=2))
        list(Book.objects.exclude(id=3))
        list(Book.objects.exclude(id=4))
        list(Book.objects.exclude(id=5))
        list(Book.objects.exclude(id=6))
        list(Book.objects.exclude(id=7))
        list(Book.objects.exclude(id=8))
        list(Book.objects.exclude(id=9))
        list(Book.objects.exclude(id=10))
