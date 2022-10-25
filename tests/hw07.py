import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
# need to use POST, GET, PUT, DELETE, WRONG methods
methods = ['GET', 'POST', 'PUT', 'DELETE', 'Wrong method', '']

for method in methods:

    get_response = requests.get(url, params={'method': f"{method}"})
    print(f"GET request with parameter {method}: ", get_response)
    print(f"Response code: {get_response.status_code}")
    print(f"Response text: {get_response.text}")
    print()

    post_response = requests.post(url, data={'method': f"{method}"})
    print(f"POST request with parameter {method}: ", post_response)
    print(f"Response code: {post_response.status_code}")
    print(f"Response text: {post_response.text}")
    print()

    put_response = requests.put(url, data={'method': f"{method}"})
    print(f"PUT request with parameter {method}: ", put_response)
    print(f"Response code: {put_response.status_code}")
    print(f"Response text: {put_response.text}")
    print()

    delete_response = requests.delete(url, data={'method': f"{method}"})
    print(f"DELETE request with parameter {method}: ", delete_response)
    print(f"Response code: {delete_response.status_code}")
    print(f"Response text: {delete_response.text}")
    print()
