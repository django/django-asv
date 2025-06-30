from django.forms import CharField, Form
from django.test import SimpleTestCase

from ...utils import bench_setup


class DummyForm(Form):
    name = CharField()


class Assertions:
    def setup(self):
        bench_setup()
        self.html = "<div><p>Hello <strong>World</strong></p></div>"
        self.response_content = "<html><body><h1>Welcome</h1><p>Test</p></body></html>"
        self.form = DummyForm(data={})
        self.test_case = SimpleTestCase()

    def time_assertContains(self):
        self.test_case.assertContains(self.response_content, "Welcome")

    def time_assertNotContains(self):
        self.test_case.assertNotContains(self.response_content, "Goodbye")

    def time_assertFormError(self):
        self.form.is_valid()
        self.test_case.assertFormError(self.form, "name", "This field is required.")

    def time_assertInHTML(self):
        self.test_case.assertInHTML("<p>Hello <strong>World</strong></p>", self.html)

    def time_assertNotInHTML(self):
        self.test_case.assertNotInHTML("<strong>Django</strong>", self.html)
