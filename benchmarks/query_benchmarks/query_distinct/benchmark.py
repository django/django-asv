from ...utils import bench_setup
from .models import Book


class QueryDistinct:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_distinct(self):
        list(Book.objects.distinct())
        list(Book.objects.distinct())
        list(Book.objects.distinct())
        list(Book.objects.distinct())
        list(Book.objects.distinct())
        list(Book.objects.distinct())
        list(Book.objects.distinct())
        list(Book.objects.distinct())
        list(Book.objects.distinct())
        list(Book.objects.distinct())
