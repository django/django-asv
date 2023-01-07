import os

from django.core.management import CommandError, call_command

import django


def bench_setup(migrate=False):
    try:
        os.environ["DJANGO_SETTINGS_MODULE"] = "benchmarks.settings"
        django.setup()
    except RuntimeError:
        pass

    if migrate is True:
        call_command("migrate", run_syncdb=True, verbosity=0)
        try:
            call_command("loaddata", "initial_data", verbosity=0)
        except CommandError as exc:
            # Django 1.10+ raises if the file doesn't exist and not
            # all benchmarks have files.
            if "No fixture named" not in str(exc):
                raise
