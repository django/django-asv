import os

import django
from django import forms

try:
    os.environ["DJANGO_SETTINGS_MODULE"] = "benchmarks.settings"
    django.setup()
except RuntimeError:
    pass


class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    form = None


class FormBenchmarks:
    def setup(self):

        self.form_clean = BookForm({"title": "hi"})

    def time_form_clean(self):
        self.form_clean.full_clean()
        self.form_clean.full_clean()
        self.form_clean.full_clean()
        self.form_clean.full_clean()
        self.form_clean.full_clean()
        self.form_clean.full_clean()
        self.form_clean.full_clean()
        self.form_clean.full_clean()
        self.form_clean.full_clean()

    def time_create_form(self):
        BookForm({"title": "a"})
        BookForm({"title": "a"})
        BookForm({"title": "a"})
        BookForm({"title": "a"})
        BookForm({"title": "a"})
        BookForm({"title": "a"})
        BookForm({"title": "a"})
        BookForm({"title": "a"})
        BookForm({"title": "a"})
        BookForm({"title": "a"})
