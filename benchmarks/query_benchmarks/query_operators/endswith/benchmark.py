from ....utils import bench_setup
from ..models import Book


class QueryFilter:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_operator_iendswith(self):
        list(Book.objects.filter(title__iendswith="Where"))
        list(Book.objects.filter(title__iendswith="the"))
        list(Book.objects.filter(title__iendswith="do not exist"))
        list(Book.objects.filter(title__iendswith="PAN"))
        list(Book.objects.filter(title__iendswith="ALICE"))
        list(Book.objects.filter(title__iendswith="charlotte"))
        list(Book.objects.filter(title__iendswith="Willows"))
        list(Book.objects.filter(title__iendswith="Rabbit"))
        list(Book.objects.filter(title__iendswith="Pooh"))
        list(Book.objects.filter(title__iendswith="Prince"))
