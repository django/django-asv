from concurrent.futures import ThreadPoolExecutor
from ...utils import bench_setup
from .models import LargeWriter, LargeNovel


# 1000 books for every 1 author
AUTHORS = 100
BOOKS = 1000 * AUTHORS


class QueryValuesForeignKeyOneThousandBooksOneHundredAuthors:
    timeout = 200

    def setup_cache(self):
        bench_setup(migrate=True)
        authors = [LargeWriter.objects.create(author=str(y)) for y in range(AUTHORS)]
        with ThreadPoolExecutor(max_workers=5) as exec:
            for book in range(BOOKS):
                exec.submit(
                    LargeNovel(title="title", author=authors[book % AUTHORS]).save
                )
        return authors

    def teardown(self, *args, **kwargs):
        LargeNovel.objects.all().delete()
        LargeWriter.objects.all().delete()

    def time_query_foreign_key_onemil(self, authors, *args, **kwargs):
        list(LargeNovel.objects.filter(author__author=authors[0].author)[:100])
        # list(LargeNovel.objects.filter(author=authors[0])[:100])

    setup_cache.timeout = 200
