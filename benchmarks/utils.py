import os
import django

def bench_setup():
    try:
        os.environ["DJANGO_SETTINGS_MODULE"] = "benchmarks.settings"
        django.setup()
    except RuntimeError:
        pass
