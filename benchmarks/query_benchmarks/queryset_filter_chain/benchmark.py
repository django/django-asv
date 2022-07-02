import datetime

from ...utils import bench_setup
from .models import Book


class FilterChain:
    def setup(self):
        bench_setup(migrate=True)

    def time_filter_chain(self):
        Book.objects.filter(title="Talent").filter(
            description__icontains="top performers"
        ).filter(author_name__startswith="Geoff").filter(
            date_created__lt=datetime.datetime(year=2010, month=1, day=1)
        ).filter(
            date_created__gte=datetime.date(year=2007, month=1, day=1)
        ).filter(
            date_published=datetime.datetime.now()
        ).filter(
            enabled=True
        )
