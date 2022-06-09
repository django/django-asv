from ...utils import bench_setup
from .models import Artist, Song


class QueryDeleteRel:
    def setup(self):
        bench_setup(migrate=True)
        self.a1 = Artist.objects.create(name="abc")
        self.a2 = Artist.objects.create(name="abc")
        self.a3 = Artist.objects.create(name="abc")
        self.a4 = Artist.objects.create(name="abc")
        self.a5 = Artist.objects.create(name="abc")
        self.a6 = Artist.objects.create(name="abc")
        self.a7 = Artist.objects.create(name="abc")
        self.a8 = Artist.objects.create(name="abc")
        self.a9 = Artist.objects.create(name="abc")
        self.a10 = Artist.objects.create(name="abc")
        for i in range(10):
            Song.objects.create(artist=self.a1, name=f"song{i}")
            Song.objects.create(artist=self.a2, name=f"song{i}")
            Song.objects.create(artist=self.a3, name=f"song{i}")
            Song.objects.create(artist=self.a4, name=f"song{i}")
            Song.objects.create(artist=self.a5, name=f"song{i}")
            Song.objects.create(artist=self.a6, name=f"song{i}")
            Song.objects.create(artist=self.a7, name=f"song{i}")
            Song.objects.create(artist=self.a8, name=f"song{i}")
            Song.objects.create(artist=self.a9, name=f"song{i}")
            Song.objects.create(artist=self.a10, name=f"song{i}")

    def time_query_del_rel(self):
        Artist.objects.all().delete()
