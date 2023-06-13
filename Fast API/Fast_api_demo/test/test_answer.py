from fastapi import status

from .fixtures import *

def test_answer_create(client, user1, pwd1, email1, subject, content_blank, content):
    question_id = 1
    url = f"/api/answer/create/{question_id}"
    response = client.post(url,
                           headers={
                               "accept": "application/json",
                               "Content-Type": "application/json"
                           })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = client.post("/api/user/create",
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

    # print(response.text)
    response = client.post("/api/question/create",
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "subject": subject,
                               "content": content,
                           })
    assert response.status_code==status.HTTP_204_NO_CONTENT

    response = client.post(f"/api/answer/create/{question_id}",
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "content": content,
                           })
    assert response.status_code==status.HTTP_204_NO_CONTENT
    
    response = client.post(url,
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "content": content_blank,
                           })
    assert response.status_code==status.HTTP_422_UNPROCESSABLE_ENTITY

    question_id = 99
    response = client.post(f"/api/answer/create/{question_id}",
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "content": content,
                           })
    assert response.status_code==status.HTTP_404_NOT_FOUND

def test_answer_update(client, user1, pwd1, email1, subject, content, content_blank):
    # 로그인하지 않은 경우
    question_id = 1
    url = "/api/answer/update"
    response = client.put(url,
                           headers={
                               "accept": "application/json",
                               "Content-Type": "application/json"
                           },
                           json={"content": content,
                                 "answer_id": 2})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = client.post("/api/user/create",
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

#     print(response.text)

    response = client.post("/api/question/create",
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "subject": subject,
                               "content": content,
                           })
    assert response.status_code==status.HTTP_204_NO_CONTENT

    response = client.post(f"/api/answer/create/{question_id}",
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "content": content,
                           })
    assert response.status_code==status.HTTP_204_NO_CONTENT
    
    response = client.put("/api/answer/update",
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "content": content_blank,
                               "answer_id": 2
                           })
    assert response.status_code==status.HTTP_422_UNPROCESSABLE_ENTITY

    response = client.put("/api/answer/update",
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "content": content,
                               "answer_id": 2
                           })
    assert response.status_code==status.HTTP_200_OK

    response = client.put("/api/answer/update",
                           headers={
                               "accept": "application/json",
                               'Authorization': token_type + ' ' + token, 
                               "Content-Type": "application/json"
                           },
                           json={"content": content,
                                 "answer_id": 99})
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_answer_delete(client, user1, pwd1, email1, subject, content, content_blank):
    # 로그인하지 않은 경우
    question_id = 2
    url = "/api/answer/delete"
    response = client.request("DELETE", url,
                           headers={
                               "accept": "application/json",
                               "Content-Type": "application/json"
                           },
                           json={"answer_id": 2})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = client.post("/api/user/create",
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

    response = client.post("/api/question/create",
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "subject": subject,
                               "content": content,
                           })
    assert response.status_code==status.HTTP_204_NO_CONTENT

    response = client.post(f"/api/answer/create/{question_id}",
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "content": content,
                           })
    assert response.status_code==status.HTTP_204_NO_CONTENT

    response = client.request("DELETE", "/api/answer/delete",
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "answer_id": 3
                           })
    assert response.status_code==status.HTTP_200_OK

    response = client.request("DELETE", "/api/answer/delete",
                           headers={
                               "accept": "application/json",
                               'Authorization': token_type + ' ' + token, 
                               "Content-Type": "application/json"
                           },
                           json={"content": content,
                                 "answer_id": 99})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
