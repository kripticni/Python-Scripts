import socket

HOST = ''
PORT = 50007              # The same port as used by the server
print('Server: ',socket.gethostbyname(''))
print('Port: ',PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))
