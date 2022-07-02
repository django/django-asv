import datetime

from django.db import models

from ...utils import bench_setup

bench_setup()


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author_name = models.TextField()
    date_created = models.DateTimeField(default=datetime.datetime.now)
    date_published = models.DateTimeField()
    enabled = models.BooleanField()
