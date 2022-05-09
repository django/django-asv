from ...utils import bench_setup
from .models import Book


class QueryExists:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_exists(self):
        # Checking for object that exists
        Book.objects.filter(id=1).exists()
        Book.objects.filter(id=2).exists()
        Book.objects.filter(id=3).exists()
        Book.objects.filter(id=4).exists()
        Book.objects.filter(id=5).exists()

        # Checking for object that does not exist
        Book.objects.filter(id=11).exists()
        Book.objects.filter(id=12).exists()
        Book.objects.filter(id=13).exists()
        Book.objects.filter(id=14).exists()
        Book.objects.filter(id=15).exists()
