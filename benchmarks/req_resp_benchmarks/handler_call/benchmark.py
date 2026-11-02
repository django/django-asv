import asyncio
import sys
from io import BytesIO

from django.core.handlers.asgi import ASGIHandler
from django.core.handlers.wsgi import WSGIHandler

from ...utils import bench_setup

PATH = "/handler-call/"


def start_response(status, response_headers, exc_info=None):
    pass


async def send(message):
    pass


def make_receive():
    messages = [{"type": "http.request", "body": b"", "more_body": False}]

    async def receive():
        if messages:
            return messages.pop()
        # The client never disconnects. The handler cancels this wait once the
        # response has been sent.
        await asyncio.Event().wait()

    return receive


class HandlerCallBench:
    """
    Call the WSGI and ASGI handlers in the same way as a server does, so that
    building the request, sending the request_started and request_finished
    signals, and producing the response are all measured.
    """

    def setup(self):
        bench_setup()
        self.wsgi_handler = WSGIHandler()
        self.wsgi_environ = {
            "REQUEST_METHOD": "GET",
            "SCRIPT_NAME": "",
            "PATH_INFO": PATH,
            "QUERY_STRING": "",
            "SERVER_NAME": "testserver",
            "SERVER_PORT": "80",
            "SERVER_PROTOCOL": "HTTP/1.1",
            "REMOTE_ADDR": "127.0.0.1",
            "wsgi.version": (1, 0),
            "wsgi.url_scheme": "http",
            "wsgi.errors": sys.stderr,
            "wsgi.multithread": False,
            "wsgi.multiprocess": False,
            "wsgi.run_once": False,
        }

        self.asgi_handler = ASGIHandler()
        self.asgi_scope = {
            "type": "http",
            "asgi": {"version": "3.0"},
            "http_version": "1.1",
            "method": "GET",
            "scheme": "http",
            "path": PATH,
            "raw_path": PATH.encode(),
            "query_string": b"",
            "root_path": "",
            "headers": [],
            "client": ("127.0.0.1", 0),
            "server": ("testserver", 80),
        }
        self.event_loop = asyncio.new_event_loop()

    def teardown(self):
        self.event_loop.close()

    def _call_wsgi_handler(self):
        # The handler mutates the environ, so give each request its own.
        environ = {**self.wsgi_environ, "wsgi.input": BytesIO()}
        response = self.wsgi_handler(environ, start_response)
        for chunk in response:
            pass
        response.close()

    def time_wsgi_handler_call(self):
        self._call_wsgi_handler()
        self._call_wsgi_handler()
        self._call_wsgi_handler()
        self._call_wsgi_handler()
        self._call_wsgi_handler()

    async def _call_asgi_handler(self):
        await self.asgi_handler(dict(self.asgi_scope), make_receive(), send)

    async def _call_asgi_handlers(self):
        await self._call_asgi_handler()
        await self._call_asgi_handler()
        await self._call_asgi_handler()
        await self._call_asgi_handler()
        await self._call_asgi_handler()

    def time_asgi_handler_call(self):
        self.event_loop.run_until_complete(self._call_asgi_handlers())
