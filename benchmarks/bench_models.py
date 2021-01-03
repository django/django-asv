import os

import django
from django.core.management import call_command

from .models import Book

try:
    os.environ["DJANGO_SETTINGS_MODULE"] = "benchmarks.settings"
    django.setup()
except RuntimeError:
    pass


def setup():
    call_command("migrate", run_syncdb=True, verbosity=0)


class ModelBenchmarks:
    def setup(self):
        self.save_existing = Book.objects.create(id=1, title="Foo")

    def teardown(self):
        Book.objects.all().delete()

    def time_model_creation(self):
        Book.objects.create(title="hi!")
        Book.objects.create(title="Bye!")
        Book.objects.create(title="hi")
        Book.objects.create(title="Bye")

    def time_model_save_existing(self):
        for i in range(0, 30):
            self.save_existing.save()

    def time_save_new(self):
        for i in range(0, 30):
            b = Book(id=i, title="Foo")
            b.save()
