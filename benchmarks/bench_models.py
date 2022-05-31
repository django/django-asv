import os

import django
from django.core.management import CommandError, call_command

from .models import Book

try:
    os.environ["DJANGO_SETTINGS_MODULE"] = "benchmarks.settings"
    django.setup()
except RuntimeError:
    pass


def setup():
    call_command("migrate", run_syncdb=True, verbosity=0)
    try:
        call_command("loaddata", "initial_data", verbosity=0)
    except CommandError as exc:
        # Django 1.10+ raises if the file doesn't exist and not
        # all benchmarks have files.
        if "No fixture named" not in str(exc):
            raise


class ModelBenchmarks:
    def setup(self):
        self.save_existing = Book.objects.get(id=1)
        self.book_count = Book.objects.count()

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
        for i in range(self.book_count, self.book_count + 30):
            b = Book(id=i, title="Foo")
            b.save()
