import random

from django.core.cache import caches
from django.core.management import call_command

from ...utils import bench_setup


class DatabaseCacheBackend:
    def setup(self):
        bench_setup()
        call_command("createcachetable", verbosity=0)
        random.seed(0)

        self.cache = caches["db"]
        self.iterations = 100
        self.int_key = "int_key"
        self.cache.set(self.int_key, 0)
        self.keys = [
            "key_{}".format(random.randint(1, 500)) for _ in range(self.iterations)
        ]
        self.values = [
            random.randint(1, 1024**1) * bytes([random.randint(0, 255)])
            for _ in range(self.iterations)
        ]

    def time_add(self):
        for key, value in zip(self.keys, self.values):
            self.cache.add(key, value)

    def time_get(self):
        for key in self.keys:
            self.cache.get(key)

    def time_set(self):
        for key, value in zip(self.keys, self.values):
            self.cache.set(key, value)

    def time_get_or_set(self):
        for key, value in zip(self.keys, self.values):
            self.cache.get_or_set(key, value)

    def time_touch(self):
        for key in self.keys:
            self.cache.touch(key)

    def time_delete(self):
        for key in self.keys:
            self.cache.delete(key)

    def time_get_many(self):
        for _ in range(self.iterations):
            self.cache.get_many(self.keys)

    def time_set_many(self):
        for _ in range(self.iterations):
            self.cache.set_many(dict(zip(self.keys, self.values)))

    def time_delete_many(self):
        for _ in range(self.iterations):
            self.cache.delete_many(self.keys)

    def time_clear(self):
        for _ in range(self.iterations):
            self.cache.clear()

    def time_incr(self):
        for _ in range(self.iterations):
            self.cache.incr(self.int_key)

    def time_decr(self):
        for _ in range(self.iterations):
            self.cache.decr(self.int_key)
