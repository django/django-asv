import datetime

from django.db import models

from ...utils import bench_setup

bench_setup()


class Converters(models.Model):
    """Both these fields have converters for sqlite"""

    date = models.DateField(default=datetime.date.today)
    decimal = models.DecimalField(default=0, max_digits=4, decimal_places=2)
