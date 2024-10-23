from concurrent.futures import ThreadPoolExecutor

from ...utils import bench_setup
from .models import Book


class QueryValues10000:
    def setup(self):
        bench_setup(migrate=True)
        with ThreadPoolExecutor(max_workers=10) as exec:
            for x in range(10000):
                exec.submit(Book(pk=x, title="title").save)

    def teardown(self):
        Book.objects.all().delete()

    def time_query_values_10000(self):
        list(Book.objects.values("title"))
