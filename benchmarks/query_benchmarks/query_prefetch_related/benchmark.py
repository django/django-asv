from ...utils import bench_setup
from .models import Author, Book


class QueryPrefetch:
    def setup(self):
        bench_setup(migrate=True)
        for i in range(20):
            a = Author.objects.create(author=f"Author {i}")
            books = [Book.objects.create(title=f"Title {j}") for j in range(3)]
            a.books.add(*books)

    def time_query_prefetch(self):
        for i in range(10):
            for a in Author.objects.prefetch_related("books"):
                list(a.books.all())
