import requests


def attack():
    url = 'http://reverse_proxy:3001'
    try:
        response = requests.get(url)
        print(f"Response from reverse proxy: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    attack()
