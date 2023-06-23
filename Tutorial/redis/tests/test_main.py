# 로그인 성공할 경우
# 비밀번호 한번 틀릴 경우
# 비밀번호 두번 틀릴 경우
# 비밀번호 틀리고 로그인에 성공할 경우 (cnt 초기화가 되야함)
# 비밀번호 5번 틀릴 경우 ()
# 블랙리스트에 들어갔는데 로그인 시도할 경우
# 블랙리스트 시간 지난 후 로그인 할 경우

def test_make_black_user(client):
    url = "127.0.0.1:8000/"
    response = client.request("GET", url,
                              json={
                                  
                              })