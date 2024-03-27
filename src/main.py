import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import base, ping
from core import config
from exception_handlers import apply_exception_handlers
from middlewares.apply_middlewares import apply_middlewares

logging.basicConfig(level=logging.INFO)


app = FastAPI(
    title=config.app_settings.app_title,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)
apply_exception_handlers(app)
apply_middlewares(app)

app.include_router(base.api_router, prefix="/api/v1")
app.include_router(ping.router, prefix="/api", tags=['ping'])

if __name__ == '__main__':
    # Приложение может запускаться командой
    # `uvicorn main:app --host 0.0.0.0 --port 8080`
    # но чтобы не терять возможность использовать дебагер,
    # запустим uvicorn сервер через python
    uvicorn.run(
        'main:app',
        host=config.PROJECT_HOST,
        port=config.PROJECT_PORT,
    )
