from typing import Optional
from pydantic import BaseModel


class BoardListBase(BaseModel):
    title: str
    index: float
    board_id: str


class BoardListUpdate(BaseModel):
    title: Optional[str]
    index: Optional[float]


class BoardListCreate(BoardListBase):
    pass


class BoardList(BoardListBase):
    id: str
