from .middleware import BlacklistMiddleware
from fastapi import FastAPI


middlewares = [BlacklistMiddleware]


def apply_middlewares(app: FastAPI):
    for middleware in middlewares:
        app.add_middleware(middleware)
