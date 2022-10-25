# payload = {"name": "User"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)

# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
# parced_response_text = response.json()
# print(parced_response_text["answer"])


from json.decoder import JSONDecodeError
import requests
import json

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
try:
    parced_response_text = response.json()
    print(parced_response_text)
except JSONDecodeError:
    print("Response is not JSON format")


string_as_json_format = '{"answer": "Hello, User"}'
obj = json.loads(string_as_json_format)
key = "answer"
if key in obj:
    print(obj)
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")
