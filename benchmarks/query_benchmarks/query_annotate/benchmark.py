from django.db.models import Count

from ...utils import bench_setup
from .models import Book


class QueryAnnotate:
    def setup(self):
        bench_setup(migrate=True)

    def time_annotate(self):
        list(Book.objects.values("title").annotate(books_total=Count("id")))
        list(Book.objects.values("title").annotate(books_total=Count("id")))
        list(Book.objects.values("title").annotate(books_total=Count("id")))
        list(Book.objects.values("title").annotate(books_total=Count("id")))
        list(Book.objects.values("title").annotate(books_total=Count("id")))
