import asyncio

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
        self.asgi_handler.load_middleware(is_async=True)
        self.event_loop = asyncio.new_event_loop()

    def teardown(self):
        self.event_loop.close()

    def time_wsgi_handler(self):
        self.wsgi_handler.get_response(self.req_factory.get("/inx-pg"))
        self.wsgi_handler.get_response(self.req_factory.get("/inx-pg"))
        self.wsgi_handler.get_response(self.req_factory.get("/inx-pg"))
        self.wsgi_handler.get_response(self.req_factory.get("/inx-pg"))
        self.wsgi_handler.get_response(self.req_factory.get("/inx-pg"))

    async def _get_asgi_responses(self):
        await self.asgi_handler.get_response_async(
            self.async_req_factory.get("/inx-pg")
        )
        await self.asgi_handler.get_response_async(
            self.async_req_factory.get("/inx-pg")
        )
        await self.asgi_handler.get_response_async(
            self.async_req_factory.get("/inx-pg")
        )
        await self.asgi_handler.get_response_async(
            self.async_req_factory.get("/inx-pg")
        )
        await self.asgi_handler.get_response_async(
            self.async_req_factory.get("/inx-pg")
        )

    def time_asgi_handler(self):
        self.event_loop.run_until_complete(self._get_asgi_responses())
