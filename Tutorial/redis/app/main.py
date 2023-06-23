import redis
from fastapi import FastAPI

import datetime


#### Cache hit, Cache miss도 활용하기####

BLACK_LIST = 1
"""[일정 시간동안 로그인 못하게 하는 유저 리스트] DB 1번을 사용"""

LOGIN_CNT_LIST = 2
"""[유저가 로그인 시도한 횟수 리스트] DB 2번을 사용"""

r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)

# app = FastAPI()

connection = r.ping()
print("connect : ", connection)

# @app.get("127.0.0.1:8000/make_black_user")
def register_black_user(username: str):
    r.select(BLACK_LIST)
    # r.set(username, datetime.datetime.now())
    r.setex(username, 60, datetime.datetime.now())
"""만료 기간 설정 후 블랙리스트에 넣기"""

def register_login_check_user(username: str):
    r.select(LOGIN_CNT_LIST)
    r.set(username, 1)

# @app.get("127.0.0.1:8000/check_black")
def check_black_user(username: str):
    # username을 통해 블랙리스트에 들어갔는지 체크
    r.select(BLACK_LIST)
    check_user = r.get(username)
    # 블랙리스트에 있을 경우
    if check_user == None:
        return True
    # 블랙리스트에 없을 경우
    else:
        return False
"""블랙리스트인지 체크하는 함수"""

# @app.get("127.0.0.1:8000/inc_cnt")
def increase_cnt(username: str):
    r.select(LOGIN_CNT_LIST)
    # user = r.get(username)
    # print(user)
    r.incr(username)
    # print(r.get(user))
"""로그인 실패시 횟수 증가 함수"""

# @app.get("127.0.0.1:8000/check_inc_cnt")
def check_login_cnt(username: str):
    # login_check_list에 username의 value가 5 이상인 경우
    # black_list에 넣고 정지시키기
    r.select(LOGIN_CNT_LIST)
    user_value = r.get(username)
    if user_value >= 5:
        make_black_user(username)
"""로그인 실패 횟수 확인 함수(5회 이상 틀렸을 경우 블랙리스트에 넣음)"""


# 로그인 성공할 경우
# 비밀번호 한번 틀릴 경우
username = "nahkim"

if check_black_user(username) == False:
    make_login_check_user(username)

# 비밀번호 두번 틀릴 경우
else:
    increase_cnt(username)
    check_login_cnt(username)


# 비밀번호 틀리고 로그인에 성공할 경우 (cnt 초기화가 되야함)
# value 변경 명령어 확인하기!!


# 비밀번호 5번 틀릴 경우 ()
for i in range(3):
    increase_cnt(username)
check_login_cnt(username)

# 블랙리스트에 들어갔는데 로그인 시도할 경우
# 블랙리스트 시간 지난 후 로그인 할 경우 -> 유효기간을 설정해서 상관없음

check_black_user(username)
make_black_user(username)
check_black_user(username)
increase_cnt(username)
check_login_cnt(username)

r.keys()
r.scan()