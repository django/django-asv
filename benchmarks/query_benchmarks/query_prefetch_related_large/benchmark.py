from ...utils import bench_setup
from .models import Author, Book


class QueryPrefetch:
    def setup(self):
        bench_setup(migrate=True)
        authors = Author.objects.bulk_create(
            [Author(author=f"Author {i}") for i in range(2000)]
        )
        books = Book.objects.bulk_create(
            [Book(title=f"Title {j}") for _ in range(2000) for j in range(3)]
        )
        Through = Author.books.through
        Through.objects.bulk_create(
            [
                Through(author=author, book=books[3 * i + j])
                for i, author in enumerate(authors)
                for j in range(3)
            ]
        )

    def teardown(self):
        Author.objects.all().delete()
        Book.objects.all().delete()

    def time_query_prefetch_large(self):
        for i in range(10):
            for a in Author.objects.prefetch_related("books"):
                list(a.books.all())
