from io import BytesIO
from itertools import repeat as rep

from django.conf import global_settings as settings
from django.core.handlers.wsgi import LimitedStream

from ...utils import bench_setup


class LimitedStreamBench:
    def setup(self):
        bench_setup()

    def bench_limitedstream_read(self, stream, size):
        while stream.read(size):
            pass

    def bench_limitedstream_readline(self, stream, size):
        while stream.readline(size):
            pass

    def prepare_stream(self, lines=1):
        part = b"a=1"
        length = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
        chunk_size = length // lines // (1 + len(part))
        generator = (rep(part, chunk_size) for _ in range(lines))
        data = b"\n".join(b"&".join(x) for x in generator)
        return LimitedStream(BytesIO(data), length)

    def time_limited_stream_read(self):
        strm = self.prepare_stream(lines=1)
        self.bench_limitedstream_read(strm, 0)
        strm = self.prepare_stream(lines=1)
        self.bench_limitedstream_read(strm, 0)
        strm = self.prepare_stream(lines=1)
        self.bench_limitedstream_read(strm, 0)

    def time_limited_stream_read_8192(self):
        strm = self.prepare_stream(lines=1)
        self.bench_limitedstream_read(strm, 8192)
        strm = self.prepare_stream(lines=1)
        self.bench_limitedstream_read(strm, 8192)
        strm = self.prepare_stream(lines=1)
        self.bench_limitedstream_read(strm, 8192)

    def time_limited_stream_readline(self):
        strm = self.prepare_stream(lines=20)
        self.bench_limitedstream_readline(strm, 0)
        strm = self.prepare_stream(lines=20)
        self.bench_limitedstream_readline(strm, 0)
        strm = self.prepare_stream(lines=20)
        self.bench_limitedstream_readline(strm, 0)

    def time_limited_stream_readline_8192(self):
        strm = self.prepare_stream(lines=20)
        self.bench_limitedstream_readline(strm, 8192)
        strm = self.prepare_stream(lines=20)
        self.bench_limitedstream_readline(strm, 8192)
        strm = self.prepare_stream(lines=20)
        self.bench_limitedstream_readline(strm, 8192)
