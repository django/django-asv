from ...utils import bench_setup
from .models import Book


class QueryCount:
    def setup(self):
        bench_setup(migrate=True)
        for i in range(10):
            Book(pk=i, title=f"foobar_{i}").save()

    def teardown(self):
        Book.objects.all().delete()

    def time_query_count(self):
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
