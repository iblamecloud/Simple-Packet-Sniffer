from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"Packet captured: {ip_src} -> {ip_dst}")

        # Print packet details
        if packet.haslayer(TCP):
            print(f"Protocol: TCP | Source Port: {packet[TCP].sport} | Destination Port: {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"Protocol: UDP | Source Port: {packet[UDP].sport} | Destination Port: {packet[UDP].dport}")
        else:
            print(f"Protocol: {packet.proto}")

        print(f"Packet Summary: {packet.summary()}")
        print("-" * 50)

print("Starting Packet Sniffer...")
sniff(prn=packet_callback, store=0, count=10)
print("Sniffing complete.")
