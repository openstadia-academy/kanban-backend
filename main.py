from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import board
import board_list
import board_task

app = FastAPI()

api_router = APIRouter()
api_router.include_router(board.router, tags=["Boards"])
api_router.include_router(board_list.router, tags=["Board Lists"])
api_router.include_router(board_task.router, tags=["Board Tasks"])

app.include_router(api_router, prefix='/api')

app.mount("/", StaticFiles(directory="static", html=True), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
