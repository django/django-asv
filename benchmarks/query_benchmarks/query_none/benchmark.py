from ...utils import bench_setup
from .models import Book


class QueryNone:
    def setup(self):
        bench_setup()

    def time_query_none(self):
        list(Book.objects.none())
        list(Book.objects.none())
        list(Book.objects.none())
        list(Book.objects.none())
        list(Book.objects.none())
        list(Book.objects.none())
        list(Book.objects.none())
        list(Book.objects.none())
        list(Book.objects.none())
        list(Book.objects.none())
        list(Book.objects.none())
