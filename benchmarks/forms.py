import os

import django
from django import forms
from django.forms.widgets import SelectDateWidget

try:
    os.environ["DJANGO_SETTINGS_MODULE"] = "benchmarks.settings"
    django.setup()
except RuntimeError:
    pass


class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    form = None


class BookFormLarge(forms.Form):
    title0 = forms.CharField(max_length=100)
    title1 = forms.CharField(max_length=100)
    title2 = forms.CharField(max_length=100)
    title3 = forms.CharField(max_length=100)
    title4 = forms.CharField(max_length=100)
    title5 = forms.CharField(max_length=100)
    title6 = forms.CharField(max_length=100)
    title7 = forms.CharField(max_length=100)
    title8 = forms.CharField(max_length=100)
    title9 = forms.CharField(max_length=100)


class FormBenchmarks:
    def setup(self):

        self.form_clean = BookForm({"title": "hi"})
        self.widget = SelectDateWidget(years=(2020,))
        self.form_render_small = BookForm()
        self.form_render_large = BookFormLarge()

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

    def time_selectdatewidget(self):
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})
        self.widget.get_context("widget", "2020-10-10", {})

    def time_small_form_render(self):
        str(self.form_render_small)
        str(self.form_render_small)
        str(self.form_render_small)
        str(self.form_render_small)
        str(self.form_render_small)
        str(self.form_render_small)
        str(self.form_render_small)
        str(self.form_render_small)
        str(self.form_render_small)
        str(self.form_render_small)

    def time_large_form_render(self):
        str(self.form_render_large)
        str(self.form_render_large)
        str(self.form_render_large)
        str(self.form_render_large)
        str(self.form_render_large)
        str(self.form_render_large)
        str(self.form_render_large)
        str(self.form_render_large)
        str(self.form_render_large)
        str(self.form_render_large)
