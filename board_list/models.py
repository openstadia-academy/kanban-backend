from pydantic import BaseModel


class BoardListBase(BaseModel):
    title: str
    board_id: str


class BoardListCreate(BoardListBase):
    pass


class BoardList(BoardListBase):
    id: str
