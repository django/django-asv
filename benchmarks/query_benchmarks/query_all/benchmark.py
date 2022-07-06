from ...utils import bench_setup
from .models import Book


class QueryAll:
    def setup(self):
        bench_setup(migrate=True)
        for i in range(3000):
            Book(pk=i, title=f"foobar_{i}").save()

    def teardown(self):
        Book.objects.all().delete()

    def time_query_all(self):
        list(Book.objects.iterator())
