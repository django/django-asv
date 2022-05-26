from ...utils import bench_setup
from .models import Book


class SaveExisting:
    def setup(self):
        bench_setup(migrate=True)
        Book.objects.create(id=1, title="Foo")

    def teardown(self):
        Book.objects.all().delete()

    def time_save_existing(self):
        b = Book.objects.get(id=1)
        for i in range(0, 30):
            b.save()
