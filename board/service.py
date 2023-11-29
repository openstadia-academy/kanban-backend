from typing import Optional, List, Dict
from uuid import uuid4

from pydantic import parse_obj_as

from data import boards
from .schemas import BoardCreate, Board


class BoardService:
    def __init__(self):
        self.boards: Dict[str, Board] = parse_obj_as(Dict[str, Board], boards)

    def get(self, id_) -> Optional[Board]:
        return self.boards.get(id_)

    def get_all(self) -> List[Board]:
        return list(self.boards.values())

    def create(self, board_in: BoardCreate) -> Board:
        id_ = str(uuid4())

        board = Board(
            id=id_,
            title=board_in.title,
        )

        self.boards[id_] = board

        return board

    def delete(self, id_: str) -> Board:
        board = self.boards.pop(id_, None)
        return board


board_service = BoardService()
