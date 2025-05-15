import requests
import json


def print_response_details(response):
    print("\n=== Response Details ===")
    print(f"Status Code: {response.status_code}")
    print("\nHeaders:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    print("\nBody:")
    try:
        print(json.dumps(response.json(), indent=2))
    except ValueError:
        print(response.text)


def send_options(url):
    """Отправка OPTIONS запроса"""
    print(f"\nSending OPTIONS request to: {url}")
    response = requests.options(url)
    print_response_details(response)


def send_get(url, params=None):
    """Отправка GET запроса"""
    print(f"\nSending GET request to: {url}")
    if params:
        print(f"\nRequest Parameters: {params}")
    response = requests.get(url, params=params)
    print_response_details(response)
    return response


def send_post(url, data=None, json_data=None):
    """Отправка POST запроса"""
    print(f"\nSending POST request to: {url}")
    if data:
        print(f"\nRequest Form Data: {data}")
    if json_data:
        print(f"\nRequest JSON Data: {json.dumps(json_data, indent=2)}")

    response = requests.post(url, data=data, json=json_data)
    print_response_details(response)
    return response


def main():
    test_url = "https://httpbin.org"
    send_options(f"{test_url}/get")
    send_get(f"{test_url}/get")
    send_get(f"{test_url}/get", params={"key1": "value1", "key2": "value2"})
    send_post(f"{test_url}/post", data={"username": "admin", "password": "admin"})
    send_post(f"{test_url}/post", json_data={"title": "Test Post", "body": "This is a test post", "userId": 1})


if __name__ == "__main__":
    main()
