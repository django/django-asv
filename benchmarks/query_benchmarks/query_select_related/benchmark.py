from ...utils import bench_setup
from .models import Book


class QuerySelectRelated:
    def setup(self):
        bench_setup(migrate=True)

    def teardown(self):
        Book.objects.all().delete()

    def time_query_select_related(self):
        for i in range(10):
            list(Book.objects.select_related("author"))
