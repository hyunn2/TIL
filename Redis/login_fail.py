import redis

r = redis.Redis()


# # 블랙리스트인지 체크 함수
# def black_list_check(username: str):
#     # username을 통해 블랙리스트에 들어갔는지 체크 후 시간이 지났는지 확인 후 삭제(분리를 하는게 나을까?)

# # 로그인 실패시 횟수 증가 함수
# def increase_cnt(username: str):
#     # login_check_list에 있는지 확인
#     # 있을 경우
#         # login_check_list에 username으로 value + 1
#     # 없을 경우
#         # username으로 login_check_list에 추가 후 value = 1

# # 로그인 실패 횟수 확인 함수(5회 이상 틀렸을 경우 블랙리스트에 넣음)
# def check_login(username: str):
#     # login_check_list에 username의 value가 5 이상인 경우
#     # black_list에 넣고 정지시키기