import redis
import datetime


#### Cache hit, Cache miss도 활용하기####

CHECK_BLOCK = 1
"""[Block 확인 번호]"""

LOGIN_CNT = 0
"""[유저가 로그인 시도한 횟수 번호]"""

# 후에 다른 곳에서도 사용한다면 class화하여 import해서 사용을 해야함!
r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)

connection = r.ping()
print("connect : ", connection)

def register_black_user(username: str):
    """로그인 불가 만료 기간 설정 및 Block True 변경"""
    r.setex(username, 60, str(datetime.datetime.now()))


def register_login_check_user(username: str):
    """black_list에 추가"""
    r.set(username, "1")

def check_black_user(username: str):
    """블랙 유저인지 체크하는 함수"""
    # username을 통해 블랙리스트에 들어갔는지 체크
    check_user = r.get(username)
    # 블랙리스트에 없을 경우
    if check_user == None:
        return False
    # 블랙리스트에 있을 경우
    else:
        return True


def increase_cnt(username: str):
    """로그인 실패시 횟수 증가 함수"""
    user_cnt = r.get(username)
    r.incr(username)


def check_login_list(username: str):
    """login_list에 있는지 확인"""
    """로그인 시도를 1회이상 했는지 확인"""
    if r.get(username) == None:
        return False
    return True

def check_login_cnt(username: str):
    """로그인 실패 횟수 확인 함수(5회 이상 틀렸을 경우 블랙리스트에 넣고 check_login_list에선 삭제)"""
    user_value = r.get(username)
    user_value = int(user_value)
    if user_value >= 5:
        register_black_user(username)
        delete_login_list(username)

def delete_login_list(username: str):
    r.delete(username)
