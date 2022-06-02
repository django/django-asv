from ...utils import bench_setup
from .models import Book


class QueryValues10000:
    def setup(self):
        bench_setup(migrate=True)
        Book.objects.bulk_create((Book(title="title") for x in range(10000)))

    def teardown(self):
        Book.objects.all().delete()

    def time_query_values_10000(self):
        list(Book.objects.values("title"))
