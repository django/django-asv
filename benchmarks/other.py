import os

import django
from django.core.management import call_command
from django.db import connection

from .models import OneField

try:
    os.environ["DJANGO_SETTINGS_MODULE"] = "benchmarks.settings"
    django.setup()
except RuntimeError:
    pass


def setup():
    call_command("migrate", run_syncdb=True, verbosity=0)


class OtherBenchmarks:
    def setup(self):
        for i in range(0, 10):
            OneField(field1=i).save()

    def teardown(self):
        pass

    def time_raw_sql(self):
        for i in range(10):
            cursor = connection.cursor()
            cursor.execute("select field1 from benchmarks_onefield")
            list(cursor.fetchall())
