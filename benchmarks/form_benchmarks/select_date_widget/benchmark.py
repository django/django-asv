from django.forms.widgets import SelectDateWidget

from ...utils import bench_setup


class DateWidget:
    def setup(self):
        bench_setup()
        self.widget = SelectDateWidget(years=(2020,))

    def time_selectdatewidget(self):
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})
