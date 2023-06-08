from typing import Union

from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated


from domain.question import question_router
from domain.user import user_router
from domain.answer import answer_router

app = FastAPI()

# Enum 사용
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get("/")
# def read_root():
#     return {"Hello" : "World"}

app.include_router(question_router.router)
app.include_router(user_router.router)
app.include_router(answer_router.router)


# @app.get("/items/{item_id}")
# def read_item(item_id: int,
#               q: Union[str, None] = None, short: bool = False):
#     item = {"item_id": item_id, "short":short}
#     return {"item_id" : item_id, "q": q, "sort":short}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name" : item.name, "item_id": item_id}

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     # 비교
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#     # 값 확인
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
    
#     return {"model_name": model_name, "message": "Have some residuals"}

# @app.get("/items/")
# async def read_tem(q: str | None = Query(max_length=4)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     return results


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
