from ...utils import bench_setup
from .models import Book


class QueryLatest:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_latest(self):
        Book.objects.latest()
        Book.objects.latest()
        Book.objects.latest()
        Book.objects.latest()
        Book.objects.latest()
        Book.objects.latest()
        Book.objects.latest()
        Book.objects.latest()
        Book.objects.latest()
        Book.objects.latest()
