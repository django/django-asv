from ...utils import bench_setup
from .models import Book


class SaveNew:
    def setup(self):
        bench_setup(migrate=True)

    def time_save_new(self):
        for i in range(0, 30):
            b = Book(id=i, title="Foo")
            b.save()
