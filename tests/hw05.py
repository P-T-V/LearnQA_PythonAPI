import json
import requests
from json.decoder import JSONDecodeError

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response)

json_text = '{"messages":[' \
            '{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
try:
    obj = json.loads(json_text)
    print(obj)
    print(obj['messages'][1]['message'])
except JSONDecodeError:
    print("Response is not JSON format")
