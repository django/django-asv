from ...utils import bench_setup


class TimeQInit:
    def setup(self):
        bench_setup()
        self.test_cases = {
            "no_args": ((), {}),
            "small_kwargs": ((), {"name": "Alice", "age": 30}),
            "large_kwargs": ((), {f"field_{i}": i for i in range(20)}),
            "args_only": (("some_condition",), {}),
            "mixed": (("cond1", "cond2"), {"name": "Bob", "active": True, "score": 99}),
        }

    def time_no_args(self):
        args, kwargs = self.test_cases["no_args"]
        return [*args, *sorted(kwargs.items())]

    def time_small_kwargs(self):
        args, kwargs = self.test_cases["small_kwargs"]
        return [*args, *sorted(kwargs.items())]

    def time_large_kwargs(self):
        args, kwargs = self.test_cases["large_kwargs"]
        return [*args, *sorted(kwargs.items())]

    def time_args_only(self):
        args, kwargs = self.test_cases["args_only"]
        return [*args, *sorted(kwargs.items())]

    def time_mixed(self):
        args, kwargs = self.test_cases["mixed"]
        return [*args, *sorted(kwargs.items())]
