from django.urls import include, path

# url_resolve, url_reverse
urlpatterns = [path("", include("benchmarks.url_benchmarks.url_resolve.urls"))]

# url_resolve_flat
urlpatterns.append(path("", include("benchmarks.url_benchmarks.url_resolve_flat.urls")))

# url_resolve_nested
urlpatterns.append(
    path("", include("benchmarks.url_benchmarks.url_resolve_nested.urls"))
)

# template_render
urlpatterns.append(
    path("", include("benchmarks.template_benchmarks.template_render.urls"))
)
