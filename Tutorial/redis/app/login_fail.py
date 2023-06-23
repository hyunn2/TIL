import redis
import datetime

BLACK_LIST = 1
"""[일정 시간동안 로그인 못하게 하는 유저 리스트] DB 1번을 사용"""

LOGIN_CNT_LIST = 2
"""[유저가 로그인 시도한 횟수 리스트] DB 2번을 사용"""

r = redis.Redis()

def register_black_user(username: str):
    r.select(BLACK_LIST)
    r.set(username, datetime.datetime.now())


def check_black_user(username: str):
    """블랙유저인지 체크하는 함수"""
    # username을 통해 블랙리스트에 들어갔는지 체크
    r.select(BLACK_LIST)
    check_user = r.get(username)

    if check_user == None:
        return False
    else:
        return True

def check_login_list(username: str):
    """로그인 시도를 1번이상 했는지 확인"""
    r.select(LOGIN_CNT_LIST)
    if r.get(username) == None:
        return False
    return True



def increase_cnt(username: str):
    """로그인 실패시 횟수 증가 함수"""
    r.select(LOGIN_CNT_LIST)
    # user = r.get(username)
    # print(user)
    r.incr(username)
    # print(r.get(user))



def check_login_cnt(username: str):
    """로그인 실패 횟수 확인 함수(5회 이상 틀렸을 경우 블랙리스트에 넣음)"""
    # login_check_list에 username의 value가 5 이상인 경우
    # black_list에 넣고 정지시키기
    r.select(LOGIN_CNT_LIST)
    user_value = r.get(username)
    if user_value >= 5:
        register_black_user(username)

        