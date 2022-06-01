from django import forms
from django.core.exceptions import ValidationError

from ...utils import bench_setup


def form_validator(title):
    if title != "hi":
        raise ValidationError("title is not hi")


class BookForm(forms.Form):
    title = forms.CharField(max_length=100, validators=[form_validator])


class FormValidate:
    def setup(self):
        bench_setup()
        self.form = BookForm({"title": "hi"})
        self.invalid_form = BookForm({"title": "abc"})

    def time_form_validate(self):
        self.form.is_valid()

    def time_form_invalid(self):
        self.invalid_form.is_valid()
