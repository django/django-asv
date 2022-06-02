from ...utils import bench_setup
from .models import Book


class QueryValues:
    def setup(self):
        bench_setup(migrate=True)

    def teardown(self):
        Book.objects.all().delete()

    def time_query_values(self):
        list(Book.objects.values("title"))
        list(Book.objects.values("title"))
        list(Book.objects.values("title"))
        list(Book.objects.values("title"))
        list(Book.objects.values("title"))
        list(Book.objects.values("title"))
        list(Book.objects.values("title"))
        list(Book.objects.values("title"))
        list(Book.objects.values("title"))
        list(Book.objects.values("title"))
