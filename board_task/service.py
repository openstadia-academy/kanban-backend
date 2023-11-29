from typing import Optional, List, Dict
from uuid import uuid4

from pydantic import parse_obj_as

from data import board_tasks
from .schemas import BoardTask, BoardTaskCreate


class BoardTaskService:
    def __init__(self):
        self.tasks: Dict[str, BoardTask] = parse_obj_as(Dict[str, BoardTask], board_tasks)

    def get(self, id_) -> Optional[BoardTask]:
        return self.tasks.get(id_, None)

    def get_all(self) -> List[BoardTask]:
        return list(self.tasks.values())

    def get_by_list_id(self, list_id: str) -> List[BoardTask]:
        return [task for task in self.tasks.values() if task.list_id == list_id]

    def create(self, task_in: BoardTaskCreate) -> BoardTask:
        id_ = str(uuid4())

        task = BoardTask(
            id=id_,
            title=task_in.title,
            description=task_in.description,
            index=task_in.index,
            list_id=task_in.list_id
        )

        self.tasks[id_] = task

        return task

    def delete(self, id_: str) -> Optional[BoardTask]:
        task = self.tasks.pop(id_, None)
        return task


board_task_service = BoardTaskService()
