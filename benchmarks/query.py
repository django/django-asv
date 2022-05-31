import os

import django
from django.core.management import call_command

from .models import Book, MultiField

try:
    os.environ["DJANGO_SETTINGS_MODULE"] = "benchmarks.settings"
    django.setup()
except RuntimeError:
    pass


def setup():
    call_command("migrate", run_syncdb=True, verbosity=0)


class QueryAll:
    def setup(self):
        for i in range(0, 3000):
            Book(pk=i, title="foobar_%s" % i).save()
        self.book_count = Book.objects.count()

    def teardown(self):
        Book.objects.all().delete()

    def time_query_all(self):
        list(Book.objects.iterator())


class QueryCount:
    def setup(self):
        for i in range(0, 10):
            Book(pk=i, title="foobar_%s" % i).save()
        self.book_count = Book.objects.count()

    def teardown(self):
        Book.objects.all().delete()

    def time_query_count(self):
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()
        Book.objects.count()


class QueryDelete:
    def setup(self):
        for i in range(0, 10):
            Book(pk=i, title="foobar_%s" % i).save()
        self.book_count = Book.objects.count()

    def teardown(self):
        Book.objects.all().delete()

    def time_query_delete(self):
        Book.objects.all().delete()


class QueryGet:
    def setup(self):
        for i in range(0, 10):
            Book(pk=i, title="foobar_%s" % i).save()
        self.book_count = Book.objects.count()

    def teardown(self):
        Book.objects.all().delete()

    def time_query_get(self):
        # This will succeed
        Book.objects.get(id=1)
        try:
            # This will fail, due to too many objects
            Book.objects.get()
        except Book.MultipleObjectsReturned:
            pass


class QueryGetOrCreate:
    def setup(self):
        for i in range(0, 10):
            Book(pk=i, title="foobar_%s" % i).save()
        self.next_id = Book.objects.count() + 1

    def teardown(self):
        Book.objects.all().delete()

    def time_query_get_or_create(self):
        # This will do a create ...
        Book.objects.get_or_create(id=self.next_id, defaults={"title": "hi"})

        # ... and this a get.
        Book.objects.get_or_create(id=self.next_id, defaults={"title": "hi"})


class QueryValuesList:
    def setup(self):
        pass

    def teardown(self):
        Book.objects.all().delete()

    def time_query_values_list(self):
        list(Book.objects.values_list("title"))


class QueryValues:
    def setup(self):
        pass

    def teardown(self):
        Book.objects.all().delete()

    def time_query_values(self):
        list(Book.objects.values("title"))


class QueryValues10000:
    def setup(self):
        Book.objects.bulk_create((Book(title="title") for x in range(10000)))

    def teardown(self):
        Book.objects.all().delete()

    def time_query_values_10000(self):
        list(Book.objects.values("title"))


class QueryUpdate:
    def setup(self):
        pass

    def teardown(self):
        Book.objects.all().delete()

    def time_query_update(self):
        Book.objects.all().update(title="z")


class QuerySelectRelated:
    def setup(self):
        pass

    def teardown(self):
        Book.objects.all().delete()

    def time_query_select_related(self):
        for i in range(20):
            list(Book.objects.select_related("author"))


class QueryRawDeferred:
    def setup(self):
        for i in range(0, 1000):
            kwargs = {}
            for j in range(1, 11):
                kwargs["field%s" % j] = "foobar_%s_%s" % (i, j)
            MultiField(**kwargs).save()

    def teardown(self):
        MultiField.objects.all().delete()

    def time_query_raw_deferred(self):
        list(MultiField.objects.raw("select id from benchmarks_multifield"))


class QueryRaw:
    def setup(self):
        for i in range(0, 1000):
            kwargs = {}
            for j in range(1, 11):
                kwargs["field%s" % j] = "foobar_%s_%s" % (i, j)
            MultiField(**kwargs).save()

    def teardown(self):
        MultiField.objects.all().delete()

    def time_query_raw_deferred(self):
        list(MultiField.objects.raw("select * from benchmarks_multifield"))
