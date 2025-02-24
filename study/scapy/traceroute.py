from scapy.all import IP, TCP, sr, RandShort

ans, unans = sr(IP(dst="44.217.196.51", ttl=(4,25),id=RandShort())/TCP(flags=0x2))

for snd, rcv in ans:
    print(snd.ttl, rcv.src, isinstance(rcv.payload, TCP))
