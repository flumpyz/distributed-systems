from datetime import datetime

from pydantic import BaseModel


class Link(BaseModel):
    url: str


class LinkCreate(Link):
    pass


class LinkInDB(Link):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
