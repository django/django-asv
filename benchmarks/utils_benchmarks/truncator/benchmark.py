from django.utils.lorem_ipsum import words
from django.utils.text import Truncator

from ...utils import bench_setup
from .djangoproject import django_project


class TruncatorBenchmark:
    def setup(self):
        bench_setup()

        self.words_50 = words(50)
        self.words_5000 = words(5000)
        self.html = django_project

    def time_words_short(self):
        truncator = Truncator(self.words_50)
        for i in range(100):
            truncator.words(10)

    def time_words_long(self):
        truncator = Truncator(self.words_5000)
        for i in range(100):
            truncator.words(100)

    def time_words_short_html(self):
        truncator = Truncator(self.html)
        for i in range(100):
            truncator.words(10, html=True)

    def time_words_long_html(self):
        truncator = Truncator(self.html)
        for i in range(100):
            truncator.words(100, html=True)

    def time_chars_short(self):
        truncator = Truncator(self.words_50)
        for i in range(100):
            truncator.chars(10)

    def time_chars_long(self):
        truncator = Truncator(self.words_5000)
        for i in range(100):
            truncator.chars(100)

    def time_chars_short_html(self):
        truncator = Truncator(self.html)
        for i in range(100):
            truncator.chars(10, html=True)

    def time_chars_long_html(self):
        truncator = Truncator(self.html)
        for i in range(100):
            truncator.chars(100, html=True)
