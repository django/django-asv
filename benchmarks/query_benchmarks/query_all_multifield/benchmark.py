from ...utils import bench_setup
from .models import MultiField


class QueryMultiField:
    def setup(self):
        bench_setup(migrate=True)
        for i in range(0, 3000):
            kwargs = {f"field{j}": f"foobar_{i}_{j}" for j in range(1, 11)}
            MultiField(**kwargs).save()

    def teardown(self):
        MultiField.objects.all().delete()

    def time_iter(self):
        list(MultiField.objects.iterator())
