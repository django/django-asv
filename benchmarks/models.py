import os

import django
from django.db import models

try:
    os.environ["DJANGO_SETTINGS_MODULE"] = "benchmarks.settings"
    django.setup()
except RuntimeError:
    pass


class Book(models.Model):
    title = models.CharField(max_length=100)


class OneField(models.Model):
    field1 = models.CharField(max_length=100)
