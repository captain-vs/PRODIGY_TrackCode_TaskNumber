from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = "Unknown"
        payload = None

        if TCP in packet:
            protocol = "TCP"
            payload = packet[TCP].payload
        elif UDP in packet:
            protocol = "UDP"
            payload = packet[UDP].payload

        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {protocol}")
        if payload:
            print(f"Payload: {bytes(payload)}")
        print("-" * 40)

def main():
    print("Starting packet sniffer...")
    sniff(filter="ip", prn=packet_callback, store=0)

if __name__ == "__main__":
    main()

