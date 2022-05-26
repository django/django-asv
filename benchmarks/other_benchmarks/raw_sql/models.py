from django.db import models

from ...utils import bench_setup

bench_setup()


class OneField(models.Model):
    field1 = models.CharField(max_length=100)
