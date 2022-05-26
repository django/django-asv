from ...utils import bench_setup
from .models import Book


class ModelCreate:
    def setup(self):
        bench_setup(migrate=True)

    def time_model_creation(self):
        Book.objects.create(title="hi")
        Book.objects.create(title="Bye!")
        Book.objects.create(title="hi")
        Book.objects.create(title="Bye")
