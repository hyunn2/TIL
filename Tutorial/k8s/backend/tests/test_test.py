from fastapi import status

# 질문 삭제
def test_question_delete(client, user1, pwd1, email1, subject, content):
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

    url = "/api/question/create"
    response = client.post(url,
                           headers={'accept': 'application/json',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'},
                           json={
                               "subject": subject,
                               "content": content,
                           })
    assert response.status_code==status.HTTP_204_NO_CONTENT

    print(user1)
    print()
    response = client.get("/api/question/list",
                          headers={'accept': 'application/json'})
    print(response.text)

    url = "/api/question/delete"

    # #########
    # response = client.delete(url,
    #                          headers={'accept': '*/*',
    #                                 'Authorization': token_type + ' ' + token, 
    #                                 'Content-Type': 'application/json'}, 
    #                         json={"question_id": 2})
    # assert response.status_code==status.HTTP_204_NO_CONTENT
    ########

    response = client.request("DELETE", url,
                             headers={'accept': '*/*',
                                    'Authorization': token_type + ' ' + token, 
                                    'Content-Type': 'application/json'}, 
                            json={"question_id": 1})
    assert response.status_code==status.HTTP_204_NO_CONTENT
