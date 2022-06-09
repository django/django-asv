from django.db import models

from ...utils import bench_setup

bench_setup()


class Artist(models.Model):
    name = models.CharField(max_length=100)


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
