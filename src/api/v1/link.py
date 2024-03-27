from typing import Any, List, Union


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session
from schemas import link_schema
from services.link import link_crud
from fastapi.responses import RedirectResponse

from services.statistic_processor import StatisticProcessor

router = APIRouter()


@router.post("/", response_model=List[link_schema.Link], status_code=status.HTTP_201_CREATED)
async def create_links(
    *,
    db: AsyncSession = Depends(get_session),
    links_in: Union[link_schema.LinkCreate, List[link_schema.LinkCreate]]
) -> Any:
    entities = []
    for link in _to_list(links_in):
        entities.append(await link_crud.create(db=db, obj_in=link))

    return entities


@router.get("/{shortened_url}")
async def redirect(
    *,
    db: AsyncSession = Depends(get_session),
    shortened_url: str,
) -> Any:
    entity = await link_crud.get(db=db, shortened_url=shortened_url)
    await link_crud.update(db=db, db_obj=entity, obj_in=StatisticProcessor.handle_link(entity))

    if not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    return RedirectResponse(entity.full_url)


@router.get("/{shortened_url}/status", response_model=link_schema.LinkStatistic, status_code=status.HTTP_200_OK)
async def get_statistics(
    *,
    db: AsyncSession = Depends(get_session),
    shortened_url: str,
) -> Any:
    entity = await link_crud.get(db=db, shortened_url=shortened_url)

    # get entity from db
    if not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    return entity


def _to_list(item: Any) -> List:
    return [item] if not isinstance(item, list) else item
