from ...utils import bench_setup
from .models import Book


class QueryValuesList:
    def setup(self):
        bench_setup(migrate=True)

    def teardown(self):
        Book.objects.all().delete()

    def time_query_values_list(self):
        list(Book.objects.values_list("title"))
        list(Book.objects.values_list("title"))
        list(Book.objects.values_list("title"))
        list(Book.objects.values_list("title"))
        list(Book.objects.values_list("title"))
        list(Book.objects.values_list("title"))
        list(Book.objects.values_list("title"))
        list(Book.objects.values_list("title"))
        list(Book.objects.values_list("title"))
        list(Book.objects.values_list("title"))
