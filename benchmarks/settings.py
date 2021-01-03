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
