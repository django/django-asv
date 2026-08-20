from ....utils import bench_setup
from ..models import Book


class QueryFilter:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_operator_startswith(self):
        list(Book.objects.filter(title__startswith="Where"))
        list(Book.objects.filter(title__startswith="the"))
        list(Book.objects.filter(title__startswith="do not exist"))
        list(Book.objects.filter(title__startswith="Peter"))
        list(Book.objects.filter(title__startswith="ALICE"))
        list(Book.objects.filter(title__startswith="charlotte"))
        list(Book.objects.filter(title__startswith="Willows"))
        list(Book.objects.filter(title__startswith="Rabbit"))
        list(Book.objects.filter(title__startswith="Pooh"))
        list(Book.objects.filter(title__startswith="Prince"))
