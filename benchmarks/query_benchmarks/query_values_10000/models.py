from django.db import models

from ...utils import bench_setup

bench_setup()


class Book(models.Model):
    default_auto_field = "django_mongodb.fields.ObjectIdAutoField"
    title = models.CharField(max_length=100)
