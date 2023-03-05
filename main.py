from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import board
import board_list
import board_task

app = FastAPI()

api_router = APIRouter()
api_router.include_router(board.router, tags=["boards"])
api_router.include_router(board_list.router, tags=["board_lists"])
api_router.include_router(board_task.router, tags=["board_tasks"])

app.include_router(api_router, prefix='/api')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
