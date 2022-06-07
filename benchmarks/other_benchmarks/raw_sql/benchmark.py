from django.db import connection

from ...utils import bench_setup
from .models import OneField


class RawSql:
    def setup(self):
        bench_setup(migrate=True)
        for i in range(0, 10):
            OneField(field1=i).save()

    def time_raw_sql(self):
        for i in range(10):
            cursor = connection.cursor()
            cursor.execute("select field1 from raw_sql_onefield")
            list(cursor.fetchall())
