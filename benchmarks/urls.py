import string

from django.urls import include, re_path

from . import views

# url_resolve


def generate_filler_patterns(num=1):
    """Returns a list of url pattern inputs for garbage views"""
    for n in range(num):
        yield re_path(r"".join((r"^", r"x" * 3 * n, r"/$")), views.basic)


urlpatterns = list(generate_filler_patterns(10))
urlpatterns.append(re_path(r"^basic/$", views.basic, name="basic"))
urlpatterns.append(re_path(r"^[a-z]*/$", views.catchall, name="catchall"))
urlpatterns.append(re_path(r"^replace/(?P<var>.*?)", views.vars, name="vars"))


# url_resolve_flat


def ok_view(request, *a, **kw):
    pass


def handler404(request):
    pass


sections = ["section%d" % i for i in range(10)]
features = ["feature%d" % i for i in range(20)]

urlpatterns += [
    re_path("^%s/%s$" % (s, f), ok_view) for s in sections for f in features
]

urlpatterns += [re_path(r"^(?P<locale>en|ru)/%s$" % f, ok_view) for f in features]

urlpatterns += [
    re_path(r"^(?P<user>\w+)/(?P<repo>\w+)/%s$" % f, ok_view) for f in features
]


# url_resolve_nested


def handler500(request):
    pass


leaf_patterns = [re_path(r"^leaf$", ok_view)]


def int2ascii(x, mod, alphabet=string.digits + string.ascii_letters):
    alphabet = alphabet[:mod]
    result = []
    while x:
        x, rem = divmod(x, mod)
        result.append(alphabet[rem])
    return ("".join(reversed(result))).rjust(1, alphabet[0])


def pattern_tree(parent, height, level):
    if height == 0:
        return leaf_patterns
    ids = [parent + int2ascii(i, level) for i in range(level)]
    return [
        re_path("^%s/" % id_, include(pattern_tree(id_, height - 1, level)))
        for id_ in ids
    ]


urlpatterns += pattern_tree("", 8, 2)

# template_render
urlpatterns += [
    re_path(r"/join/?$", views.join, name="join"),
    re_path(r"/login/?$", views.login, name="login"),
    re_path(r"/logout/?$", views.logout, name="logout"),
]
