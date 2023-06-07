from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from domain.question import question_router

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# @app.get("/")
# def read_root():
#     return {"Hello" : "World"}

app.include_router(question_router.router)


# @app.get("/items/{item_id}")
# def read_item(item_id: int,
#               q: Union[str, None] = None):
#     return {"item_id" : item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name" : item.name, "item_id": item_id}

# # 순차적으로 확인하고 동작하기 때문에 /user/me를 먼저 선언해야함!
# # 반대로 선언하게 된다면 매개변수 user_id의 값을 "me"로 하여 연결할 수 있기 때문
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "The current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# # @app.get("/users/{gender}")
# # def get_user(gender: str):
# #     return "Type is String"

# # @app.get("/users/{num}")
# # def get_user(num: int):
# #     return "Type is int"
