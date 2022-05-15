from django.db import models
from django.core.exceptions  import ValidationError
from django.utils.translation import gettext_lazy as _
from ...utils import bench_setup

bench_setup()

def validate_name(name):
    if name != 'abc':
        raise ValidationError(
            _('%(name)s is not abc'),
            params={'name': name},
        )

class Song(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])