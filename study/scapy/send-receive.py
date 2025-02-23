from scapy.all import Ether, IP, TCP, UDP, ICMP, sendp, send, sr

l2packet = Ether()/IP(dst="192.168.1.1",ttl=(7,12))
sendp(l2packet)

l3packet = IP(dst='192.168.1.1',ttl=(13,15))/ICMP()
plist = send(l3packet, return_packets=True)
for received in plist:
    print(f"Received: {received.summary()}")
    print(f"Raw Payload: {received.show()}")

response, unanswered = sr(l3packet, timeout=2)

for sent, received in response:
    print(f"Sent: {sent.summary()}")
    print(f"Received: {received.summary()}")
    print(f"Raw Payload: {received.show()}")


