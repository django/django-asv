from ....utils import bench_setup
from ..models import Book


class QueryFilter:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_operator_istartswith(self):
        list(Book.objects.filter(title__istartswith="Where"))
        list(Book.objects.filter(title__istartswith="the"))
        list(Book.objects.filter(title__istartswith="do not exist"))
        list(Book.objects.filter(title__istartswith="Peter"))
        list(Book.objects.filter(title__istartswith="ALICE"))
        list(Book.objects.filter(title__istartswith="charlotte"))
        list(Book.objects.filter(title__istartswith="Willows"))
        list(Book.objects.filter(title__istartswith="Rabbit"))
        list(Book.objects.filter(title__istartswith="Pooh"))
        list(Book.objects.filter(title__istartswith="Prince"))
