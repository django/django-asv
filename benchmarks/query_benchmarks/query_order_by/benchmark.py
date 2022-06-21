from ...utils import bench_setup
from .models import Book


class QueryOrderBy:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_order_by(self):
        list(Book.objects.order_by("id"))
        list(Book.objects.order_by("id"))
        list(Book.objects.order_by("id"))

        list(Book.objects.order_by("title"))
        list(Book.objects.order_by("title"))
        list(Book.objects.order_by("title"))
