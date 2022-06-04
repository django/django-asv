from ...utils import bench_setup
from .models import Book


class QueryDates:
    def setup(self):
        bench_setup(migrate=True)

    def time_query_dates(self):
        list(Book.objects.dates("created_date", "year", "ASC"))
        list(Book.objects.dates("created_date", "year", "DESC"))
        list(Book.objects.dates("created_date", "month", "ASC"))
        list(Book.objects.dates("created_date", "month", "DESC"))
        list(Book.objects.dates("created_date", "day", "ASC"))
        list(Book.objects.dates("created_date", "day", "DESC"))
