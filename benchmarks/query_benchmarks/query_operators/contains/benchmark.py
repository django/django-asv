from ....utils import bench_setup
from ..models import Book


class QueryFilter:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_operator_contains(self):
        list(Book.objects.filter(title__contains="in"))
        list(Book.objects.filter(title__contains="the"))
        list(Book.objects.filter(title__contains="do not exist"))
        list(Book.objects.filter(title__contains="Peter"))
        list(Book.objects.filter(title__contains="ALICE"))
        list(Book.objects.filter(title__contains="charlotte"))
        list(Book.objects.filter(title__contains="Willows"))
        list(Book.objects.filter(title__contains="Rabbit"))
        list(Book.objects.filter(title__contains="Pooh"))
        list(Book.objects.filter(title__contains="Prince"))
