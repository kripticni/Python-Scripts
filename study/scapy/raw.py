from scapy.all import IP, TCP, sr, RawVal

int_max = 2**15 - 1
int_max = int_max.to_bytes(2, byteorder='big')
packet = IP(len=RawVal(int_max), src="192.168.1.8", dst="192.168.1.1")
response, unans = sr(packet)
