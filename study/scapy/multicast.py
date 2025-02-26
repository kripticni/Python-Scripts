from scapy.config import conf
from scapy.all import IP, ICMP, sr, IPv6, ICMPv6EchoRequest

conf.checkIPaddr = False

l3multiv4 = IP(dst="224.0.0.1%enp8s0")/ICMP()
response, unanswered = sr(l3multiv4, multi=True, timeout=10)

l3multiv6 = IPv6(dst="ff02::1%enp8s0")/ICMPv6EchoRequest()
response, unanswered = sr(l3multiv6, multi=True, timeout=10)
