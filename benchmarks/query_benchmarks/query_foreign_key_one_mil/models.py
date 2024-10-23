from django.db import models

from ...utils import bench_setup

bench_setup()

class LargeWriter(models.Model):
    author = models.CharField(max_length=100)


class LargeNovel(models.Model):
    default_auto_field = "django_mongodb.fields.ObjectIdAutoField"
    title = models.CharField(max_length=100)
    author = models.ForeignKey(LargeWriter, on_delete=models.CASCADE)
