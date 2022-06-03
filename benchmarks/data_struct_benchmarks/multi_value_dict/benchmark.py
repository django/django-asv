import copy

from django.utils.datastructures import MultiValueDict

from ...utils import bench_setup


class MultiValueDictBench:
    def setup(self):
        bench_setup()
        self.case = {"a": ["a"], "b": ["a", "b"], "c": ["a", "b", "c"]}
        self.update = {"a": ["a"], "b": ["a", "b"], "c": ["a", "b", "c"]}

    def time_multi_value_dict(self):
        caseDict = MultiValueDict(self.case)

        caseDict["a"]
        caseDict["b"]
        caseDict["c"]

        caseDict.update(self.update)
        copy.copy(caseDict)
        copy.deepcopy(caseDict)

        caseDict.items()
        caseDict.lists()
        for i in caseDict:
            i

        caseDict["a"] = "A"
        caseDict["b"] = "B"
        caseDict["c"] = "C"
