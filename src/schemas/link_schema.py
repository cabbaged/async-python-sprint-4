from datetime import datetime

from pydantic import BaseModel, HttpUrl


class LinkBase(BaseModel):
    pass


class LinkCreate(LinkBase):
    full_url: HttpUrl


class LinkUpdate(LinkBase):
    usages: int
    last_usage: datetime


class LinkInDBBase(LinkBase):
    full_url: str
    shortened_url: str
    created_at: datetime

    class Config:
        orm_mode = True


class Link(LinkInDBBase):
    pass


class LinkInDB(LinkInDBBase):
    pass


class LinkStatistic(LinkInDBBase):
    usages: int
    last_usage: datetime
