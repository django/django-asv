from ...utils import bench_setup
from .models import Book


class QueryUpdate:
    def setup(self):
        bench_setup(migrate=True)

    def teardown(self):
        Book.objects.all().delete()

    def time_query_update(self):
        for i in range(1, 11):
            Book.objects.all().update(title=f"{i}")
