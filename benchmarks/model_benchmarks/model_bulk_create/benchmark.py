from ...utils import bench_setup
from .models import Book


class ModelCreate:
    def setup(self):
        bench_setup(migrate=True)

    def time_model_bulk_creation(self):
        Book.objects.bulk_create([Book(title=f"Book {i}") for i in range(1_000)])
