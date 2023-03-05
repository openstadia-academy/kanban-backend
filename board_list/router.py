from typing import List

from fastapi import APIRouter, HTTPException

from .models import BoardList, BoardListCreate
from .service import board_list_service

router = APIRouter()


@router.get('/boards/{board_id}/lists', response_model=List[BoardList])
def read_lists_by_board(board_id: str):
    return board_list_service.get_by_board_id(board_id)


@router.get('/lists', response_model=List[BoardList])
def read_board_lists():
    return board_list_service.get_all()


@router.get('/lists/{list_id}', response_model=BoardList)
def read_board_list(list_id: str):
    board_list = board_list_service.get(list_id)

    if not board_list:
        raise HTTPException(status_code=404, detail="List not found")

    return board_list


@router.post('/lists', response_model=BoardList)
def create_board_list(
        list_in: BoardListCreate,
):
    board_list = board_list_service.create(list_in)
    return board_list


@router.delete('/lists/{list_id}', response_model=BoardList)
def delete_board_list(list_id: str):
    board_list = board_list_service.delete(list_id)

    if not board_list:
        raise HTTPException(status_code=404, detail="List not found")

    return board_list
