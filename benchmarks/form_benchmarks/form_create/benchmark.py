from django import forms

from ...utils import bench_setup


class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    form = None


class FormCreate:
    def setup(self):
        bench_setup()

    def time_form_create(self):
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
