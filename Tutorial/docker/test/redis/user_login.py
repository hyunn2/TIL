import redis
import datetime


#### Cache hit, Cache miss도 활용하기####

BLACK_LIST = 2
"""[일정 시간동안 로그인 못하게 하는 유저 리스트]"""

LOGIN_CNT_LIST = 1
"""[유저가 로그인 시도한 횟수 리스트]"""

# 후에 다른 곳에서도 사용한다면 class화하여 import해서 사용을 해야함!
r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)

connection = r.ping()
print("connect : ", connection)

def register_black_user(username: str):
    """만료 기간 설정 후 블랙리스트에 넣기"""
    r.select(BLACK_LIST)
    r.setex(username, 60, str(datetime.datetime.now()))


def register_login_check_user(username: str):
    """login_check_list에 추가"""
    r.select(LOGIN_CNT_LIST)
    r.set(username, "1")

def check_black_user(username: str):
    """블랙 유저인지 체크하는 함수"""
    # username을 통해 블랙리스트에 들어갔는지 체크
    r.select(BLACK_LIST)
    check_user = r.get(username)
    # 블랙리스트에 없을 경우
    if check_user == None:
        return False
    # 블랙리스트에 있을 경우
    else:
        return True


def increase_cnt(username: str):
    """로그인 실패시 횟수 증가 함수"""
    r.select(LOGIN_CNT_LIST)
    user_cnt = r.get(username)
    r.incr(username)


def check_login_list(username: str):
    """login_list에 있는지 확인"""
    """로그인 시도를 1회이상 했는지 확인"""
    r.select(LOGIN_CNT_LIST)
    if r.get(username) == None:
        return False
    return True

def check_login_cnt(username: str):
    """로그인 실패 횟수 확인 함수(5회 이상 틀렸을 경우 블랙리스트에 넣고 check_login_list에선 삭제)"""
    r.select(LOGIN_CNT_LIST)
    user_value = r.get(username)
    user_value = int(user_value)
    if user_value >= 5:
        register_black_user(username)
        delete_login_list(username)

def delete_login_list(username: str):
    r.select(LOGIN_CNT_LIST)
    r.delete(username)
