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
        self.int_key = "int_key"
        self.cache.set(self.int_key, 0)

    def time_add(self):
        for _ in range(100):
            self.cache.add(self.random_key(), self.random_binary())

    def time_get(self):
        for _ in range(100):
            self.cache.get(self.random_key())

    def time_set(self):
        for _ in range(100):
            self.cache.set(self.random_key(), self.random_binary())

    def time_get_or_set(self):
        for _ in range(100):
            self.cache.get_or_set(self.random_key(), self.random_binary())

    def time_touch(self):
        for _ in range(100):
            self.cache.touch(self.random_key())

    def time_delete(self):
        for _ in range(100):
            self.cache.delete(self.random_key())

    def time_get_many(self):
        for _ in range(100):
            self.cache.get_many([self.random_key() for x in range(100)])

    def time_set_many(self):
        for _ in range(100):
            self.cache.set_many(
                {self.random_key(): self.random_binary() for x in range(100)}
            )

    def time_delete_many(self):
        for _ in range(100):
            self.cache.delete_many([self.random_key() for x in range(100)])

    def time_clear(self):
        for _ in range(100):
            self.cache.clear()

    def time_incr(self):
        for _ in range(100):
            self.cache.incr(self.int_key)

    def time_decr(self):
        for _ in range(100):
            self.cache.decr(self.int_key)

    def random_key(self):
        return "key_{}".format(random.randint(1, 500))

    def random_binary(self):
        return random.randint(1, 1024**1) * random.randint(0, 255)
