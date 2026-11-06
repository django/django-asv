from django.test import RequestFactory
from django.utils.translation import get_language_from_request

from ...utils import bench_setup

ACCEPT_LANGUAGE_HEADERS = [
    # No language preference.
    "",
    # Known languages.
    "af",
    "ar",
    "az",
    "bg",
    "be",
    "bn",
    "br",
    "bs",
    "ca",
    "cs",
    "cy",
    "da",
    "en",
    "en-gb",
    # Region-specific variants of known languages (e.g. fr-fr -> fr).
    "fr-fr",
    "fy-nl",
    "nl-nl",
    "en-us",
    # A generic language that only matches a variant (zh -> zh-hans).
    "zh",
    # Multiple preferences.
    "en-us,en",
    "nl-be,nl",
    "de-ch,de;q=0.9,en;q=0.8,*;q=0.5",
    # Unknown or invalid languages.
    "INVALID",
    "UNKNOWN",
    "NONE",
    "KLINGON",
]


class LocaleFromRequest:
    def setup(self):
        bench_setup()
        request_factory = RequestFactory()
        self.requests = [
            request_factory.get("/", HTTP_ACCEPT_LANGUAGE=header)
            for header in ACCEPT_LANGUAGE_HEADERS
        ]

    def time_get_language_from_request(self):
        for request in self.requests:
            get_language_from_request(request)
