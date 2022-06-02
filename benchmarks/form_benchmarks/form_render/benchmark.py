from django import forms

from ...utils import bench_setup


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


class FormRender:
    def setup(self):
        bench_setup()
        self.form_render_small = BookForm()
        self.form_render_large = BookFormLarge()

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
