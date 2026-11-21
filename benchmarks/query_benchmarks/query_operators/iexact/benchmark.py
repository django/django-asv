from ....utils import bench_setup
from ..models import Book


class QueryFilter:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_operator_exact(self):
        list(Book.objects.filter(title__exact="Alice in Wonderland"))
        list(Book.objects.filter(title__exact="Peter Pan"))
        list(Book.objects.filter(title__exact="do not exist"))
        list(Book.objects.filter(title__exact="Peter"))
        list(Book.objects.filter(title__exact="ALICE"))
        list(Book.objects.filter(title__exact="charlotte"))
        list(Book.objects.filter(title__exact="Willows"))
        list(Book.objects.filter(title__exact="Rabbit"))
        list(Book.objects.filter(title__exact="Pooh"))
        list(Book.objects.filter(title__exact="Prince"))
