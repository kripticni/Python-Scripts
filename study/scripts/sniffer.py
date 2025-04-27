import socket
from scapy.all import Ether, IP, TCP, UDP, ICMP
#import ssl

sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

interface = "enp8s0"

try:
    while True:
        raw_data, addr = sniffer_socket.recvfrom(65535)
        packet = Ether(raw_data)
        #print(packet.show2())
        #print(packet.show())
        #print(packet.json())

        print("="*75)
        print(packet.summary())
        print(f"Ethernet: {packet.src} -> {packet.dst} | Type: {packet.type}")

        if packet.haslayer(IP):
            ip_layer = packet[IP]
            print(f"IP: {ip_layer.src} -> {ip_layer.dst} | Protocol: {ip_layer.proto}")

            if packet.haslayer(TCP):
                tcp_layer = packet[TCP]
                print(f"TCP: {tcp_layer.sport} -> {tcp_layer.dport} | Flags: {tcp_layer.flags}")
            elif packet.haslayer(UDP):
                udp_layer = packet[UDP]
                print(f"UDP: {udp_layer.sport} -> {udp_layer.dport}")
            elif packet.haslayer(ICMP):
                icmp_layer = packet[ICMP]
                print(f"ICMP: Type: {icmp_layer.type} | Code: {icmp_layer.code}")
        print("="*75)

except KeyboardInterrupt:
    sniffer_socket.close()
    exit()
#except:
#    print('error fetching')
#    exit()

