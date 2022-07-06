from django.db import models

from ...utils import bench_setup

bench_setup()


class Author(models.Model):
    author = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)
