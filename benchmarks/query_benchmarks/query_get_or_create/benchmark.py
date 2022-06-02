from ...utils import bench_setup
from .models import Book


class QueryGetOrCreate:
    def setup(self):
        bench_setup(migrate=True)
        self.next_id = Book.objects.count() + 1

    def teardown(self):
        Book.objects.all().delete()

    def time_query_get_or_create(self):
        # This will do a create ...
        Book.objects.get_or_create(id=self.next_id, defaults={"title": "hi"})
        Book.objects.get_or_create(id=self.next_id + 1, defaults={"title": "hi"})
        Book.objects.get_or_create(id=self.next_id + 2, defaults={"title": "hi"})

        # ... and this a get.
        Book.objects.get_or_create(id=self.next_id, defaults={"title": "hi"})
        Book.objects.get_or_create(id=self.next_id + 1, defaults={"title": "hi"})
        Book.objects.get_or_create(id=self.next_id + 2, defaults={"title": "hi"})
