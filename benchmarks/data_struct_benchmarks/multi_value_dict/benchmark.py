import copy

from django.utils.datastructures import MultiValueDict

from ...utils import bench_setup


class MultiValueDictBench:
    def setup(self):
        bench_setup()
        self.case = {"a": ["a"], "b": ["a", "b"], "c": ["a", "b", "c"]}
        self.update = {"a": ["a"], "b": ["a", "b"], "c": ["a", "b", "c"]}

    def time_multi_value_dict(self):
        for i in range(1000):
            case_dict = MultiValueDict(self.case)

            case_dict["a"]
            case_dict["b"]
            case_dict["c"]

            case_dict.update(self.update)
            copy.copy(case_dict)
            copy.deepcopy(case_dict)

            case_dict.items()
            case_dict.lists()
            for i in case_dict:
                i

            case_dict["a"] = "A"
            case_dict["b"] = "B"
            case_dict["c"] = "C"
