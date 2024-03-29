from django.urls import include, path

# url_resolve
urlpatterns = [
    path("url-resolve/", include("benchmarks.url_benchmarks.url_resolve.urls"))
]

# url_reverse
urlpatterns.append(
    path(
        "url-reverse/",
        include("benchmarks.url_benchmarks.url_reverse.urls", namespace="url_reverse"),
    )
)

# url_resolve_flat
urlpatterns.append(
    path(
        "url-resolve-flat/", include("benchmarks.url_benchmarks.url_resolve_flat.urls")
    )
)

# url_resolve_nested
urlpatterns.append(
    path(
        "url-resolve-nested/",
        include("benchmarks.url_benchmarks.url_resolve_nested.urls"),
    )
)

# template_render
urlpatterns.append(
    path(
        "template-render/",
        include("benchmarks.template_benchmarks.template_render.urls"),
    )
)

# default_middleware
urlpatterns.append(
    path("", include("benchmarks.req_resp_benchmarks.default_middleware.urls"))
)

# http methods
urlpatterns.append(
    path("", include("benchmarks.req_resp_benchmarks.http_methods.urls"))
)
