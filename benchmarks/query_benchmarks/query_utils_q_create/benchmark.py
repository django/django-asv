from django.db.models import Q

from ...utils import bench_setup


class QCreate:
    def setup(self):
        bench_setup()
        self.children_no_args = []
        self.children_small = [("name", "Alice"), ("age", 30)]
        self.children_large = [(f"field_{i}", i) for i in range(20)]
        self.children_args_only = ["some_condition"]
        self.children_mixed = [
            "cond1",
            "cond2",
            ("name", "Bob"),
            ("active", True),
            ("score", 99),
        ]

    def time_create_no_args(self):
        for _ in range(100):
            Q().create(children=self.children_no_args)

    def time_create_small(self):
        for _ in range(100):
            Q().create(children=self.children_small)

    def time_create_large(self):
        for _ in range(100):
            Q().create(children=self.children_large)

    def time_create_args_only(self):
        for _ in range(100):
            Q().create(children=self.children_args_only)

    def time_create_mixed(self):
        for _ in range(100):
            Q().create(children=self.children_mixed)
