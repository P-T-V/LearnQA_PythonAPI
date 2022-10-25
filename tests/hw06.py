import requests


response = requests.get("https://playground.learnqa.ru/api/long_redirect")
amount = len(response.history)
print("Amount of response.history:", amount)
for i in range(amount):
    print_response = response.history[i]
    print()
    print(i+1, "response.url:", print_response.url)
    print(i+1, "response.status_code:", print_response.status_code)
