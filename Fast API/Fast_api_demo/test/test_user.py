from .fixtures import *

def test_read_main_case1(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg" : "Hello World"}


##### User #####

# 회원 가입
# # 성공
# def test_user_create_case(client):
#     response = client.post("/api/user/create",
#                            headers={},
#                            json={
#                                "username": "string",
#                                "password1": "string",
#                                "password2": "string",
#                                "email": "user@example.com"
#                            })
#     assert response.status_code==200


# # 아이디 중복
# def test_user_create_case1():
#     response = client.post("/api/user/create",
#                            headers={},
#                            json={
#                                "username": "string",
#                                "password1": "string",
#                                "password2": "string",
#                                "email": "user@example.com"
#                            })
#     assert response.status_code==409

# # 이메일 중복
# def test_user_create_case1():
#     response = client.post("/api/user/create",
#                            headers={},
#                            json={
#                                "username": "string",
#                                "password1": "string",
#                                "password2": "string",
#                                "email": "user@example.com"
#                            })
#     assert response.status_code==409

# # 비밀번호 불일치
# def test_user_create_case2():
#     response = client.post("/api/user/create",
#                            headers={},
#                            json={
#                                "username": "string",
#                                "password1": "string",
#                                "password2": "string",
#                                "email": "user@example.com"
#                            })
#     assert response.status_code==

# # ======================================================================

# # 로그인
# # 성공
# def test_login_for_access_token1():
#     response = client.post("/api/user/create",
#                            headers={},
#                            json={
#                                "username": "string",
#                                "password1": "string",
#                                "password2": "string",
#                                "email": "user@example.com"
#                            })
#     assert response.status_code==401

# # 존재하지 않는 아이디
# def test_login_for_access_token():
#     response = client.post("/api/user/create",
#                            headers={},
#                            json={
#                                "username": "string",
#                                "password1": "string",
#                                "password2": "string",
#                                "email": "user@example.com"
#                            })
#     assert response.status_code==
#     assert response.json() == {
#         "access_token": access_token,
#         "token_type": "bearer",
#         "username": user.username
#     }

# # 잘못된 비밀번호
# def test_login_for_access_token1():
#     response = client.post("/api/user/create",
#                            headers={},
#                            json={
#                                "username": "string",
#                                "password1": "string",
#                                "password2": "string",
#                                "email": "user@example.com"
#                            })
#     assert response.status_code==401


# # ======================================================================

# # 토큰
# # 완료
# def test_get_current_user():

# # 토큰이 유효하지 않는 경우
# # 아이디가 없는 경우
# def test_get_current_user():

# # 토큰이 유효하지 않는 경우
# # 토큰 에러
# def test_get_current_user():

# # 토큰이 유효하지 않는 경우
# # 로그인을 안한 경우?
# def test_get_current_user():
