from ...utils import bench_setup
from .models import Book


class QueryRelatedIn:
    def setup(self):
        bench_setup()
        self.author_ids = list(range(100000))

    def time_query_related_in(self):
        Book.objects.filter(author__in=self.author_ids)
