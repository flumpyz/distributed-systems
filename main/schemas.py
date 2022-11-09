from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Link(BaseModel):
    url: str


class LinkCreate(Link):
    pass


class LinkUpdate(BaseModel):
    status: str


class LinkInDB(BaseModel):
    id: int
    status: Optional[str]
    url: str
    created_at: datetime

    class Config:
        orm_mode = True
