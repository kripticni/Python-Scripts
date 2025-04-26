from scapy.all import IP, UDP, DNS, DNSQR, sr1

packet = IP(dst="192.168.1.1") / UDP() / DNS(rd=1, qd=DNSQR(qname="www.google.com"))
response = sr1(packet)
print(response.show())
