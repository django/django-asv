from ...utils import bench_setup
from .models import Book


class QueryDelete:
    def setup(self):
        bench_setup(migrate=True)
        for i in range(10):
            Book(pk=i, title=f"foobar_{i}").save()

    def time_query_delete(self):
        Book.objects.all().delete()
