import socket
from scapy.all import Ether, IP, UDP, TCP, DNS, DNSQR, sr1

packet = IP(dst="192.168.1.1")/UDP()/DNS(rd=1, qd=DNSQR(qname="www.httpbin.org"))
response = sr1(packet)
ip = response[DNS].an.rdata

response = bytearray(1024)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 80))
s.settimeout(10)
s.sendall(b"GET /get HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n")
s.recvfrom_into(response, 1024)

packet = Ether(response)

print("="*75)
print("Server ip: ", ip)
print(packet.json())
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
