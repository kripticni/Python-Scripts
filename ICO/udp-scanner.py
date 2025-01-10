from socket import *

ip = str(input('Insert ip: '))
data = 'Hello World!'.encode()

s = socket(AF_INET, SOCK_DGRAM)
s.settimeout(1)

for port in range(0,65535):
    try:
        s.sendto(data,(ip,port))
        response = s.recvfrom(1024)
        print('Open port is, ', str(port))
    except:
        continue
