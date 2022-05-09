from ...utils import bench_setup
from .models import Book


class QueryFilter:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_filter(self):
        list(Book.objects.filter(id=1))
        list(Book.objects.filter(id=2))
        list(Book.objects.filter(id=3))
        list(Book.objects.filter(id=4))
        list(Book.objects.filter(id=5))
        list(Book.objects.filter(id=6))
        list(Book.objects.filter(id=7))
        list(Book.objects.filter(id=8))
        list(Book.objects.filter(id=9))
        list(Book.objects.filter(id=10))
