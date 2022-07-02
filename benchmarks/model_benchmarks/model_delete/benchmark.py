from ...utils import bench_setup
from .models import Book


class ModelDelete:
    def setup(self):
        bench_setup(migrate=True)
        for i in range(10):
            Book.objects.create(title=f"foobar{i}")

    def time_delete(self):
        for i in range(10):
            Book.objects.filter(title=f"foobar{i}").delete()
