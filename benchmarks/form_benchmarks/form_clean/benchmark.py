from django import forms

from ...utils import bench_setup


class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    form = None


class FormClean:
    def setup(self):
        bench_setup()
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
