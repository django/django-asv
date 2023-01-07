from django.core.handlers.asgi import ASGIHandler
from django.core.handlers.wsgi import WSGIHandler
from django.test import AsyncRequestFactory, RequestFactory

from ...utils import bench_setup


class DefaultMiddleWareBench:
    def setup(self):
        bench_setup()
        self.req_factory = RequestFactory()
        self.wsgi_handler = WSGIHandler()
        self.wsgi_handler.load_middleware()

        self.async_req_factory = AsyncRequestFactory()
        self.asgi_handler = ASGIHandler()
        self.asgi_handler.load_middleware()

    def time_wsgi_handler(self):
        self.wsgi_handler.get_response(self.req_factory.get("/inx-pg"))
        self.wsgi_handler.get_response(self.req_factory.get("/inx-pg"))
        self.wsgi_handler.get_response(self.req_factory.get("/inx-pg"))
        self.wsgi_handler.get_response(self.req_factory.get("/inx-pg"))
        self.wsgi_handler.get_response(self.req_factory.get("/inx-pg"))

    async def time_asgi_handler(self):
        await self.asgi_handler.get_response(self.async_req_factory.get("/inx-pg"))
        await self.asgi_handler.get_response(self.async_req_factory.get("/inx-pg"))
        await self.asgi_handler.get_response(self.async_req_factory.get("/inx-pg"))
        await self.asgi_handler.get_response(self.async_req_factory.get("/inx-pg"))
        await self.asgi_handler.get_response(self.async_req_factory.get("/inx-pg"))
