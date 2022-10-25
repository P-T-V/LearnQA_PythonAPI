import requests


payload2 = {"login": "secret_login", "password": "secret_pass2"}
response2 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload2)
print("\nresponse2.text: ", response2.text)
print("response2.status_code: ", response2.status_code)
print("response2.cookies: ", dict(response2.cookies))


payload = {"login": "secret_login", "password": "secret_pass"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
print("response.text: ", response.text)
print("response.status_code: ", response.status_code)
print("response.cookies: ", dict(response.cookies))
print("response.headers: ", response.headers)


payload3 = {"login": "secret_login", "password": "secret_pass"}
response3 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload3)

cookie_value = response3.cookies.get('auth_cookie')

cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

response4 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print("\nresponse4.text: ", response4.text)
