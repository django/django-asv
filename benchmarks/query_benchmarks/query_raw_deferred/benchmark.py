from ...utils import bench_setup
from .models import MultiField


class QueryRawDeferred:
    def setup(self):
        bench_setup(migrate=True)
        for i in range(1000):
            kwargs = {f"field{j}": f"foobar_{i}_{j}" for j in range(1, 11)}
            MultiField(**kwargs).save()

    def teardown(self):
        MultiField.objects.all().delete()

    def time_query_raw_deferred(self):
        list(MultiField.objects.raw("select id from query_raw_deferred_multifield"))
