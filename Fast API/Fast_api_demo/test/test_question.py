from .test_user import test_user_create_case
from fastapi import status

from .fixtures import *

# 질문 리스트
def test_question_list(client):
    url = "/api/question/list"
    response = client.get(url,
                          headers={'accept': 'application/json'})

    print(response.text)
    assert response.status_code == status.HTTP_200_OK

# 질문 상세
# 유효하지 않는 question_id 일 경우
def test_question_detail(client):
    question_id = 0
    url = f'/api/question/list/{question_id}'
    response = client.get(url,
                          headers={'accept': 'application/json'})

    assert response.status_code == status.HTTP_404_NOT_FOUND

# 질문 생성
# 로그인하지 않고 생성 불가
def test_question_create(client, subject, content):
    url = "/api/question/create"
    response = client.post(url,
                           headers={'Content-Type': 'application/json',
                                    'accept': 'application/json',
                                    'Authorization': ''
                                    },
                           json={
                               "subject": subject,
                               "content": content,
                           })
    assert response.status_code==status.HTTP_401_UNAUTHORIZED

# 질문 생성
# 로그인 후 생성
def test_question_create1(client, subject, content, user1, pwd1, email1):
    
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

    response = client.post("/api/user/login",
                           headers={'accept': 'application/json',
                                    'Content-Type': 'application/x-www-form-urlencoded'},
                           data={
                               "username": user1,
                               "password": pwd1,
                               })
    assert response.status_code==status.HTTP_200_OK

    token = response.json().get("access_token")
    token_type = str(response.json().get("token_type").capitalize())

    # print("token! :", token)
    # print("token type! :", token_type)
    # print("Authorization :",token_type + ' ' + token)

    url = "/api/question/create"
    response = client.post(url,
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "subject": subject,
                               "content": content,
                           })
    assert response.status_code==status.HTTP_200_OK

    question_id = 1
    url = f'/api/question/detail/{question_id}'
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK



# 질문 생성
# 주어진 파라미터가 빈값인 경우
def test_question_create2(client, subject_blank, content_blank, subject, content, user1, pwd1, email1):
    
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

    response = client.post("/api/user/login",
                           headers={'accept': 'application/json',
                                    'Content-Type': 'application/x-www-form-urlencoded'},
                           data={
                               "username": user1,
                               "password": pwd1,
                               })
    assert response.status_code==status.HTTP_200_OK

    token = response.json().get("access_token")
    token_type = str(response.json().get("token_type").capitalize())

    # print("token! :", token)
    # print("token type! :", token_type)
    # print("Authorization :",token_type + ' ' + token)

    url = "/api/question/create"
    response = client.post(url,
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "subject": subject,
                               "content": content_blank,
                           })
    assert response.status_code==status.HTTP_422_UNPROCESSABLE_ENTITY

    url = "/api/question/create"
    response = client.post(url,
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "subject": subject_blank,
                               "content": content,
                           })
    assert response.status_code==status.HTTP_422_UNPROCESSABLE_ENTITY


# 질문 수정
# 완료
def test_question_update(client, subject, content, user1, pwd1, email1):
    url = "/api/question/update"
    response = client.put(url,
                          headers={
                              'accept': 'application/json',
                              'Authorization': '',
                              'Content-Type': 'application/json'},
                              json={
                                  "subject": subject,
                                  "content": content,
                                  "question_id": 0
                              })
    assert response.status_code==status.HTTP_401_UNAUTHORIZED

# 로그인 추가해야함
def test_question_update1(client, subject_blank, content_blank, user1, pwd1, email1):
    url = "/api/question/update"
    response = client.put(url,
                          headers={
                              'accept': 'application/json',
                              'Authorization': '',
                              'Content-Type': 'application/json'},
                              json={
                                  "subject": subject_blank,
                                  "content": content_blank,
                                  "question_id": 0
                              })
    assert response.status_code==status.HTTP_401_UNAUTHORIZED


# 질문 수정
# 빈 값인 경우
# def test_question_update():

# 질문 수정
# 질문 등록자가 아닌 경우
# def test_question_update():

# 질문 수정
# 데이터가 없는 경우
# def test_question_update():

# 질문 삭제
# 완료
# def test_question_delete():

# 질문 삭제
# 질문 등록자가 아닌 경우(권한이 없는 경우)
# def test_question_delete():

# 질문 삭제
# 데이터가 없는 경우
# def test_question_delete():
