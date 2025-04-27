import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
s.send(cmd)

data = str("")
while True:
    recieved = s.recv(512)
    data = data + str(recieved.decode())
    if (len(recieved) < 1):
        break
header, body = data.split('\r\n\r\n',1)
print(body)
s.close()
