from fastapi import APIRouter

from .link import router as link_router

api_router = APIRouter()
api_router.include_router(link_router, prefix="/link", tags=["link"])
