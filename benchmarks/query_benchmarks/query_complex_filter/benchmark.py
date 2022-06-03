from ...utils import bench_setup
from .models import Book


class QueryCmplxFilter:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_complex_filter(self):
        Book.objects.complex_filter({"pk": 1})
        Book.objects.complex_filter({"pk": 2})
        Book.objects.complex_filter({"pk": 3})
        Book.objects.complex_filter({"pk": 4})
        Book.objects.complex_filter({"pk": 5})
        Book.objects.complex_filter({"pk": 6})
        Book.objects.complex_filter({"pk": 7})
        Book.objects.complex_filter({"pk": 8})
        Book.objects.complex_filter({"pk": 9})
        Book.objects.complex_filter({"pk": 10})
