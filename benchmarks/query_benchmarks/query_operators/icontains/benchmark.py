from ....utils import bench_setup
from ..models import Book


class QueryFilter:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_operator_icontains(self):
        list(Book.objects.filter(title__icontains="in"))
        list(Book.objects.filter(title__icontains="the"))
        list(Book.objects.filter(title__icontains="do not exist"))
        list(Book.objects.filter(title__icontains="Peter"))
        list(Book.objects.filter(title__icontains="ALICE"))
        list(Book.objects.filter(title__icontains="charlotte"))
        list(Book.objects.filter(title__icontains="Willows"))
        list(Book.objects.filter(title__icontains="Rabbit"))
        list(Book.objects.filter(title__icontains="Pooh"))
        list(Book.objects.filter(title__icontains="Prince"))
