# DoS Attack Project

This project demonstrates a Denial of Service (DoS) attack using Docker and Docker Compose. It includes an attacked server, a reverse proxy, and an attacker. This setup is for educational purposes only, demonstrating the impact and methods of DoS attacks in a controlled environment.

## Project Structure

- `attacked_server`: A simple server that is the target of the attacks.
- `reverse_proxy`: A reverse proxy that forwards requests to the attacked server.
- `attacker`: The attacking component that performs various DoS attacks.

## Prerequisites

- Docker
- Docker Compose
- Wireshark (for analyzing network traffic)

## Setup Instructions

### In VSCode:

1. **Compose the containers**:
   
   ```docker-compose up --build```

2. **Run tcpdump listener in the attacked server**:
   
   ```docker exec -it cyber_proj-attacked_server-1 tcpdump -i any -w /tmp/packets_attacked_server.pcap```

3. **Run tcpdump listener in the reverse proxy**:
   
   ```docker exec -it cyber_proj-reverse_proxy-1 tcpdump -i any -w /tmp/packets_proxy.pcap```

4. **Run tcpdump listener in the attacker**:
   
   ```docker exec -it cyber_proj-attacker-1 tcpdump -i any -w /tmp/packets_attacker.pcap```

5. **Run the attack**:
   - Open the attacker shell:
     
     ```docker exec -it cyber_proj-attacker-1 /bin/bash```
     
   - Run the attack script:
     
     ```python attack.py```

   ***Wait for response before proceeding to step 6.***

6. **Stop the listener on the attacked server**:
    
   ```ctrl + c```

7. **Stop the listener on the reverse proxy**:
    
   ```ctrl + c```

8. **Stop the listener on the attacker**:
    
   ```ctrl + c```

9. **Optional: Inspect file content before importing to host**:
   - Attacked server:
     
     ```docker exec -it cyber_proj-attacked_server-1 tcpdump -r /tmp/packets_attacked_server.pcap```
     
   - Reverse proxy:
     
     ```docker exec -it cyber_proj-reverse_proxy-1 tcpdump -r /tmp/packets_proxy.pcap```
     
   - Attacker:
     
     ```docker exec -it cyber_proj-attacker-1 tcpdump -r /tmp/packets_attacker.pcap```

10. **Import the captured packets to the host**:
    ```
    docker cp cyber_proj-attacked_server-1:/tmp/packets_attacked_server.pcap ./packets_attacked_server.pcap
    docker cp cyber_proj-attacker-1:/tmp/packets_attacker.pcap ./packets_attacker.pcap
    docker cp cyber_proj-reverse_proxy-1:/tmp/packets_proxy.pcap ./packets_proxy.pcap

### In Wireshark:

11. Open the generated files:
   
   ```File -> Open -> Select the `.pcap` files generated.```

## Note

This project is a simulation of DoS attacks for educational purposes only. It is designed to run in a sandbox environment using Docker and Docker Compose to prevent any unintended damage.

## Restarting the Attacked Server

To restart the attacked server before changing the target, use the following command:
```docker-compose restart attacker```

## Security Notice

Performing DoS attacks on systems without permission is illegal and unethical. Use this project responsibly and only in a controlled environment for learning purposes.
