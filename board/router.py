from typing import List

from fastapi import APIRouter, HTTPException

from .schemas import Board, BoardCreate
from .service import board_service

router = APIRouter()


@router.get('/boards', response_model=List[Board])
def read_boards():
    return board_service.get_all()


@router.get('/boards/{board_id}', response_model=Board)
def read_board(board_id: str):
    board = board_service.get(board_id)

    if not board:
        raise HTTPException(status_code=404, detail="Item not found")

    return board


@router.post('/boards', response_model=Board)
def create_board(
        board_in: BoardCreate,
):
    board = board_service.create(board_in)
    return board


@router.delete('/boards/{board_id}', response_model=Board)
def delete_board(board_id: str):
    board = board_service.delete(board_id)

    if not board:
        raise HTTPException(status_code=404, detail="Item not found")

    return board
