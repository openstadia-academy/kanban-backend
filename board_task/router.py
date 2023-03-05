from typing import List

from fastapi import APIRouter, HTTPException

from .models import BoardTask, BoardTaskCreate
from .service import board_task_service

router = APIRouter()


@router.get('/lists/{list_id}/tasks', response_model=List[BoardTask])
def read_tasks_by_list_id(list_id: str):
    return board_task_service.get_by_list_id(list_id)


@router.get('/tasks', response_model=List[BoardTask])
def read_tasks():
    return board_task_service.get_all()


@router.get('/tasks/{task_id}', response_model=BoardTask)
def read_task_by_id(task_id: str):
    board_task = board_task_service.get(task_id)

    if not board_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return board_task


@router.post('/tasks', response_model=BoardTask)
def create_task(
        task_in: BoardTaskCreate,
):
    board_task = board_task_service.create(task_in)
    return board_task


@router.delete('/tasks/{task_id}', response_model=BoardTask)
def delete_task_by_id(task_id: str):
    board_task = board_task_service.delete(task_id)

    if not board_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return board_task
