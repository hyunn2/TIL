from fastapi import status

from .fixtures import *


# 회원 가입
def test_user_create_case(client, user1, user2, pwd1, pwd2, email1, email2):
    url = "/api/user/create"
    response = client.post(url,
                           headers={'Content-Type': 'application/json'},
                           json={
                               "username": user1,
                               "password1": pwd1,
                               "password2": pwd1,
                               "email": email1 + "@example.com"
                           })
    assert response.status_code==status.HTTP_204_NO_CONTENT

    # 아이디 중복
    response = client.post(url,
                           headers={'Content-Type': 'application/json'},
                           json={
                               "username": user1,
                               "password1": pwd1,
                               "password2": pwd1,
                               "email": email2 + "@example.com"
                           })
    assert response.status_code==status.HTTP_409_CONFLICT

    # 이메일 중복
    response = client.post(url,
                           headers={'Content-Type': 'application/json'},
                           json={
                               "username": user2,
                               "password1": pwd2,
                               "password2": pwd2,
                               "email": email1 + "@example.com"
                           })
    assert response.status_code==status.HTTP_409_CONFLICT

    # 빈값 비허용
    response = client.post(url,
                           headers={'Content-Type': 'application/json'},
                           json={
                               "username": "",
                               "password1": pwd1,
                               "password2": pwd2,
                               "email": email2 + "@example.com"
                           })
    assert response.status_code==status.HTTP_422_UNPROCESSABLE_ENTITY

    # 빈값 비허용
    response = client.post(url,
                           headers={'Content-Type': 'application/json'},
                           json={
                               "username": user2,
                               "password1": "",
                               "password2": pwd2,
                               "email": email2 + "@example.com"
                           })
    assert response.status_code==status.HTTP_422_UNPROCESSABLE_ENTITY

    # 빈값 비허용
    response = client.post(url,
                           headers={'Content-Type': 'application/json'},
                           json={
                               "username": user2,
                               "password1": pwd1,
                               "password2": "",
                               "email": email2 + "@example.com"
                           })
    assert response.status_code==status.HTTP_422_UNPROCESSABLE_ENTITY

    # 빈값 비허용
    response = client.post(url,
                           headers={'Content-Type': 'application/json'},
                           json={
                               "username": user2,
                               "password1": pwd1,
                               "password2": pwd2,
                               "email": ""
                           })
    assert response.status_code==status.HTTP_422_UNPROCESSABLE_ENTITY

    # 비밀번호 불일치
    response = client.post(url,
                           headers={'Content-Type': 'application/json'},
                           json={
                               "username": user2,
                               "password1": pwd1,
                               "password2": pwd2,
                               "email": email2 + "@example.com"
                           })
    assert response.status_code==status.HTTP_422_UNPROCESSABLE_ENTITY

# 로그인
    # 존재하지 않는 아이디
    response = client.post("/api/user/login",
                           headers={'accept': 'application/json',
                                    'Content-Type': 'application/x-www-form-urlencoded'},
                           data={
                               "username": user2,
                               "password": pwd1,
                               })

    assert response.status_code==status.HTTP_401_UNAUTHORIZED

    # 잘못된 비밀번호
    response = client.post("/api/user/login",
                           headers={'accept': 'application/json',
                                    'Content-Type': 'application/x-www-form-urlencoded'},
                           data={
                               "username": user1,
                               "password": pwd2,
                               })
    
    assert response.status_code==status.HTTP_401_UNAUTHORIZED

    # 로그인 성공
    response = client.post("/api/user/login",
                           headers={'accept': 'application/json',
                                    'Content-Type': 'application/x-www-form-urlencoded'},
                           data={
                               "username": user1,
                               "password": pwd1,
                               })
    # print(user1, pwd1)
    # print(response.json().get("access_token"))
    # print()
    # print(response.text)
    assert response.status_code==status.HTTP_200_OK


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
