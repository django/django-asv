from ...utils import bench_setup
from .models import Book


class QueryCmplxFilter:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_complex_filter(self):
        for i in range(0, 10):
            Book.objects.complex_filter({"pk": f"{i}"})
