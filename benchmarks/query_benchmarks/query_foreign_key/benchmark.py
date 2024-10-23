from ...utils import bench_setup
from .models import Writer, Novel


class QueryValuesForeignKey:
    def setup(self):
        bench_setup(migrate=True)
        authors = [Writer.objects.create(author=str(y)) for y in range(10)]
        for x in range(10):
            Novel(title="title", author=authors[x]).save()
        self.authors = authors

    def teardown(self):
        Novel.objects.all().delete()
        Writer.objects.all().delete()

    def time_query_foreign_key_author_author(self):
        for author in self.authors:
            list(Novel.objects.filter(author__author=author.author))

    def time_query_foreign_key_author_id(self):
        for author in self.authors:
            list(Novel.objects.filter(author=author))
