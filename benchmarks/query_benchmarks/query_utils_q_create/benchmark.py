import inspect
from collections import Counter

from ...utils import bench_setup
from django.db.models import Q
from .models import Content


class QueryQCreateCallsites:
    def setup(self):
        bench_setup(migrate=True)

    def teardown(self):
        Content.objects.all().delete()

    def time_q_internal_create_calls(self):
        original_create = Q.create
        call_count = 0
        call_sites = Counter()

        def profiled_create(cls, *args, **kwargs):
            nonlocal call_count, call_sites
            call_count += 1

            frame = inspect.stack()[1]
            call_sites[(frame.filename, frame.lineno, frame.function)] += 1

            # Normalize arguments
            if args:
                children = args[0]
                connector = args[1] if len(args) > 1 else kwargs.get("connector", Q.AND)
                negated = args[2] if len(args) > 2 else kwargs.get("negated", False)
            else:
                children = kwargs.get("children", [])
                connector = kwargs.get("connector", Q.AND)
                negated = kwargs.get("negated", False)

            return original_create.__func__(cls, children, connector, negated)

        Q.create = classmethod(profiled_create)

        for i in range(2000):
            q1 = Q(a=i)
            q2 = Q(b=i % 5)
            q3 = q1 & q2
            q4 = q3 | Q(c=i)

        Q.create = original_create

        self.call_count = call_count
        self.call_sites = call_sites
        print("CALL COUNT:", call_count)
        print("CALL SITES:", call_sites)

        return {"call_count": call_count, "call_sites": call_sites}
