from ...utils import bench_setup
from .models import Book


class QueryInBulk:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_in_bulk(self):
        Book.objects.in_bulk([1])
        Book.objects.in_bulk([1, 2])
        Book.objects.in_bulk([1, 2, 3])
        Book.objects.in_bulk([1, 2, 3, 4])
        Book.objects.in_bulk([1, 2, 3, 4, 5])
