from django.core.checks import run_checks

from ...utils import bench_setup


class SystemChecks:
    def setup(self):
        bench_setup(migrate=True)

    def time_checks(self):
        run_checks(include_deployment_checks=True, databases=("default",))
