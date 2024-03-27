from typing import Any

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session

router = APIRouter()


@router.get("/ping", status_code=status.HTTP_200_OK)
async def ping_db(
    *,
    db: AsyncSession = Depends(get_session)
) -> Any:
    """
    Ping database.
    """
    import logging
    logging.getLogger('').info('ping')
    await db.execute('select 1')
