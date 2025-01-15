"""
Usage: Passes a request along a chain of handlers.
"""

from fastapi import FastAPI, Request
from typing import Callable


class Handler:
    def set_next(self, handler: "Handler") -> "Handler":
        self.next_handler = handler
        return handler

    def handle(self, request: Request):  # type: ignore
        if hasattr(self, "next_handler"):
            return self.next_handler.handle(request)  # type: ignore
        return None


class AuthenticationHandler(Handler):
    def handle(self, request: Request):  # type: ignore
        token = request.headers.get("Authorization")
        if token == "valid_token":
            return super().handle(request)  # type: ignore
        return {"error": "Unauthorized"}


class LoggingHandler(Handler):
    def handle(self, request: Request):  # type: ignore
        print(f"Logging request from {request.client.host}")  # type: ignore
        return super().handle(request)  # type: ignore


app = FastAPI()


@app.middleware("http")
async def process_request(request: Request, call_next: Callable):  # type: ignore
    authentication = AuthenticationHandler()
    logging = LoggingHandler()
    authentication.set_next(logging)

    response = authentication.handle(request)  # type: ignore
    if response:
        return response  # type: ignore

    return await call_next(request)  # type: ignore
