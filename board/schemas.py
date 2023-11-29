from pydantic import BaseModel


class BoardBase(BaseModel):
    title: str


class BoardCreate(BoardBase):
    pass


class Board(BoardBase):
    id: str
