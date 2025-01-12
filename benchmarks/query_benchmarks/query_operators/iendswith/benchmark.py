from ....utils import bench_setup
from ..models import Book


class QueryFilter:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_operator_endswith(self):
        list(Book.objects.filter(title__endswith="Where"))
        list(Book.objects.filter(title__endswith="the"))
        list(Book.objects.filter(title__endswith="do not exist"))
        list(Book.objects.filter(title__endswith="PAN"))
        list(Book.objects.filter(title__endswith="ALICE"))
        list(Book.objects.filter(title__endswith="charlotte"))
        list(Book.objects.filter(title__endswith="Willows"))
        list(Book.objects.filter(title__endswith="Rabbit"))
        list(Book.objects.filter(title__endswith="Pooh"))
        list(Book.objects.filter(title__endswith="Prince"))
