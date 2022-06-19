from django.core.exceptions import ValidationError
from django.db import models

from ...utils import bench_setup

bench_setup()


def validate_name(name):
    if name != "abc":
        raise ValidationError


class Song(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
