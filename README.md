# Simple-Packet-Sniffer
This is a **network packet sniffer** built using **Python** and the **Scapy** library. It captures and analyzes network packets in real time, displaying relevant details like source and destination IP addresses, protocol types, and port numbers.
## Features:
- Captures live network packets.
- Supports multiple protocols: **IP, TCP, UDP, and ICMP**.
- Displays **source/destination IPs**, **ports**, and **protocol details**.
- Lightweight and easy to use.
- Works on **Linux, macOS, and Windows** (requires admin/root privileges).
## How To use:
- Clone the repository
- Instal the dependencies
  ```bash
  pip install scapy
  ```
- Run the script (Requires administrator/root privileges):
  - Linux/macOS
    ```bash
    sudo python packet_sniffer.py
    ```
  - Windows (Run Command Prompt as Administrator):
    ```bash
    python packet_sniffer.py
    ```
# Example 
```bash
Starting Packet Sniffer...
Packet captured: 192.168.0.1 -> 192.168.0.2
Protocol: TCP | Source Port: 443 | Destination Port: 56789
Packet Summary: 192.168.0.1:443 > 192.168.0.2:56789
--------------------------------------------------
...
Sniffing complete.
```

# Permissions
- Administrator/root access is required to capture packets at the network level.
- Use this tool responsibly and only on networks you have permission to monitor.

