from ....utils import bench_setup
from ..models import Book


class QueryFilter:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_operator_iexact(self):
        list(Book.objects.filter(title__iexact="Alice in Wonderland"))
        list(Book.objects.filter(title__iexact="Peter Pan"))
        list(Book.objects.filter(title__iexact="do not exist"))
        list(Book.objects.filter(title__iexact="Peter"))
        list(Book.objects.filter(title__iexact="ALICE"))
        list(Book.objects.filter(title__iexact="charlotte"))
        list(Book.objects.filter(title__iexact="Willows"))
        list(Book.objects.filter(title__iexact="Rabbit"))
        list(Book.objects.filter(title__iexact="Pooh"))
        list(Book.objects.filter(title__iexact="Prince"))
