import requests


class Test_hw_11:

    def test_cookie(self):
        response = requests.get(
            "https://playground.learnqa.ru/api/homework_cookie"
        )
        print(response.cookies)
        assert response.cookies['HomeWork'] == 'hw_value', f"Incorrect response cookie: {response.cookies['HomeWork']}"
        print(f"HomeWork = {response.cookies['HomeWork']}")
