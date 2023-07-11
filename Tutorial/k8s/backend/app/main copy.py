import asyncio

from fastapi import FastAPI, WebSocket, status
from starlette.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocketDisconnect

from datetime import datetime

from domain.question import question_router
from domain.user import user_router
from domain.answer import answer_router

app = FastAPI()

# cors
# 서버 실행시 url이 어떤건지 보고 그거쓰기
origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConnectionManager:
    def __init__(self):
        self.activate_connections: list[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.activate_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.activate_connections.remove(websocket)
    
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def broadcast(self, message: str):
        for connection in self.activate_connections:
            await connection.send_text(message)

manager = ConnectionManager()

# websocket 생성
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    # 소켓 연결
    await manager.connect(websocket)
    try:
        while True:
            # 데이터 받고 보내기
            data = await websocket.receive_text()
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} : {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


app.include_router(question_router.router)
app.include_router(user_router.router)
app.include_router(answer_router.router)
