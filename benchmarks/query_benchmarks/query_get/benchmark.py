from ...utils import bench_setup
from .models import Book


class QueryGet:
    def setup(self):
        bench_setup(migrate=True)
        for i in range(10):
            Book(pk=i, title=f"foobar_{i}").save()

    def teardown(self):
        Book.objects.all().delete()

    def time_query_get(self):
        for i in range(10):
            # This will succeed
            Book.objects.get(id=1)
            try:
                # This will fail, due to too many objects
                Book.objects.get()
            except Book.MultipleObjectsReturned:
                pass
