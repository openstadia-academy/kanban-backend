from typing import Optional, List, Dict
from uuid import uuid4

from pydantic import parse_obj_as

from data import board_lists
from .models import BoardListCreate, BoardList


class BoardListService:
    def __init__(self):
        self.lists: Dict[str, BoardList] = parse_obj_as(Dict[str, BoardList], board_lists)

    def get(self, id_) -> Optional[BoardList]:
        return self.lists.get(id_, None)

    def get_all(self) -> List[BoardList]:
        return list(self.lists.values())

    def get_by_board_id(self, board_id: str) -> List[BoardList]:
        return [list_ for list_ in self.lists.values() if list_.board_id == board_id]

    def create(self, list_in: BoardListCreate) -> BoardList:
        id_ = str(uuid4())

        list_ = BoardList(
            id=id_,
            board_id=list_in.board_id,
            title=list_in.title,
        )

        self.lists[id_] = list_

        return list_

    def delete(self, id_: str) -> Optional[BoardList]:
        list_ = self.lists.pop(id_, None)
        return list_


board_list_service = BoardListService()
