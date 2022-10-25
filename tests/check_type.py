import requests


response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
print(response.text)

response2 = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
print(response2.text)

response3 = requests.delete("https://playground.learnqa.ru/api/check_type")
print(response3.text)

response4 = requests.put("https://playground.learnqa.ru/api/check_type")
print(response4.text)

response5 = requests.post("https://playground.learnqa.ru/api/check_type")
print("\nresponse5.status_code: ", response5.status_code)

response6 = requests.post("https://playground.learnqa.ru/api/get_500")
print("\nresponse6.status_code: ", response6.status_code)
print("response6.text: ", response6.text)

response7 = requests.post("https://playground.learnqa.ru/api/something")
print("\nresponse7.status_code:", response7.status_code)
print("\nresponse7.text:", response7.text)

response8 = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print("\nresponse8.status_code:", response8.status_code)

response8 = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response8.history[0]
second_response = response8
print("first_response.url:", first_response.url)
print("\nsecond_response.url:", second_response.url)
print("second_response.status_code:", response8.status_code)
