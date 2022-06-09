from django.http import HttpResponse
from django.urls import re_path


def ok_view(request, *a, **kw):
    return HttpResponse()


def handler404(request):
    return HttpResponse()


sections = ["section%d" % i for i in range(10)]
features = ["feature%d" % i for i in range(20)]

urlpatterns = [re_path("^%s/%s$" % (s, f), ok_view) for s in sections for f in features]

urlpatterns += [re_path(r"^(?P<locale>en|ru)/%s$" % f, ok_view) for f in features]

urlpatterns += [
    re_path(r"^(?P<user>\w+)/(?P<repo>\w+)/%s$" % f, ok_view) for f in features
]
