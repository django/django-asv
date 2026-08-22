from django.db import models

from ...utils import bench_setup

bench_setup()


class Author(models.Model):
    pass


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
