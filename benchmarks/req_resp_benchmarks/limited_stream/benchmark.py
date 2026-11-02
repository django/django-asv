from io import BytesIO

from django.conf import settings
from django.core.handlers.wsgi import LimitedStream

from ...utils import bench_setup


def make_body(lines):
    """
    Build a form-encoded body of about DATA_UPLOAD_MAX_MEMORY_SIZE bytes split
    over the given number of lines.
    """
    part = b"a=1"
    chunk_size = settings.DATA_UPLOAD_MAX_MEMORY_SIZE // lines // (len(part) + 1)
    return b"\n".join(b"&".join([part] * chunk_size) for _ in range(lines))


class LimitedStreamBench:
    def setup(self):
        bench_setup()
        self.single_line = make_body(lines=1)
        self.multiple_lines = make_body(lines=20)

    def _read(self, data, size):
        stream = LimitedStream(BytesIO(data), len(data))
        while stream.read(size):
            pass

    def _readline(self, data, size):
        stream = LimitedStream(BytesIO(data), len(data))
        while stream.readline(size):
            pass

    def time_read_single_line(self):
        self._read(self.single_line, None)

    def time_read_8192_single_line(self):
        self._read(self.single_line, 8192)

    def time_readline_single_line(self):
        self._readline(self.single_line, None)

    def time_readline_8192_single_line(self):
        self._readline(self.single_line, 8192)

    def time_read_multiple_lines(self):
        self._read(self.multiple_lines, None)

    def time_read_8192_multiple_lines(self):
        self._read(self.multiple_lines, 8192)

    def time_readline_multiple_lines(self):
        self._readline(self.multiple_lines, None)

    def time_readline_8192_multiple_lines(self):
        self._readline(self.multiple_lines, 8192)
