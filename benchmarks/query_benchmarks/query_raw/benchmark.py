from ...utils import bench_setup
from .models import MultiField


class QueryRaw:
    def setup(self):
        bench_setup(migrate=True)
        for i in range(1000):
            kwargs = {f"field{j}": f"foobar_{i}_{j}" for j in range(1, 11)}
            MultiField(**kwargs).save()

    def teardown(self):
        MultiField.objects.all().delete()

    def time_query_raw(self):
        list(MultiField.objects.raw("select * from query_raw_multifield"))
