from ...utils import bench_setup
from django.db import models

class Startup:

    def time_startup(self):
        bench_setup()
