import socket

HOST = '' #all available ifaces
PORT = 50007 #random non privilaged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Host: ",socket.gethostbyname(''))
    print("On port: ",PORT)
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break 
            conn.sendall(data)
s.close()
exit()
