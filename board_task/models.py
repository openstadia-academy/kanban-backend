from typing import Optional

from pydantic import BaseModel


class BoardTaskBase(BaseModel):
    title: str
    description: Optional[str]
    index: float
    list_id: str


class BoardTaskCreate(BoardTaskBase):
    pass


class BoardTask(BoardTaskBase):
    id: str
