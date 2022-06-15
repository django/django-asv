import os

ALLOWED_HOSTS = ["*"]

DATABASE_ENGINE = "sqlite3"
DATABASE_NAME = ":memory:"

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"},
}

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "benchmarks",
    "benchmarks.query_benchmarks.query_all_multifield",
    "benchmarks.template_benchmarks.template_render",
    "benchmarks.template_benchmarks.template_compilation",
    "benchmarks.query_benchmarks.query_annotate",
    "benchmarks.query_benchmarks.query_all_conv",
    "benchmarks.query_benchmarks.query_complex_filter",
    "benchmarks.query_benchmarks.query_dates",
    "benchmarks.query_benchmarks.query_delete_related",
    "benchmarks.model_benchmarks.model_create",
    "benchmarks.model_benchmarks.model_save_new",
    "benchmarks.model_benchmarks.model_save_existing",
    "benchmarks.other_benchmarks.raw_sql",
    "benchmarks.query_benchmarks.query_distinct",
    "benchmarks.url_benchmarks.url_resolve",
    "benchmarks.url_benchmarks.url_resolve_flat",
    "benchmarks.url_benchmarks.url_resolve_nested",
    "benchmarks.url_benchmarks.url_reverse",
    "benchmarks.query_benchmarks.query_exclude",
    "benchmarks.query_benchmarks.query_exists",
    "benchmarks.query_benchmarks.query_in_bulk",
    "benchmarks.query_benchmarks.query_latest",
]

SECRET_KEY = "NOT REALLY SECRET"

ROOT_URLCONF = "benchmarks.urls"

TEMPLATE_DIRS = (os.path.abspath(os.path.join(os.path.dirname(__file__), "templates")),)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.abspath(os.path.join(os.path.dirname(__file__), "templates")),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
