from django.urls import re_path

from . import views


def generate_filler_patterns(num=1):
    """Returns a list of url pattern inputs for garbage views"""
    for n in range(num):
        yield re_path(r"".join((r"^", r"x" * 3 * n, r"/$")), views.basic)


urlpatterns = list(generate_filler_patterns(10))
urlpatterns.append(re_path(r"^basic/$", views.basic, name="basic"))
urlpatterns.append(re_path(r"^[a-z]*/$", views.catchall, name="catchall"))
urlpatterns.append(re_path(r"^replace/(?P<var>.*?)", views.vars, name="vars"))
