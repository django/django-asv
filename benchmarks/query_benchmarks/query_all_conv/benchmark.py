from ...utils import bench_setup
from .models import Converters


class QueryAllConv:
    def setup(self):
        bench_setup(migrate=True)
        for i in range(0, 100):
            Converters().save()

    def time_query_all_conv(self):
        list(Converters.objects.iterator())
