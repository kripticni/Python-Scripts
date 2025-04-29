import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 51256))
s.listen(1)
print("Opened socket on 0.0.0.0:51256")

conn, addr = s.accept()
print(f"Connected by {addr}:{conn}")
while True:
    input = conn.recv(512) + b"\n"
    if not input:
        break
    _ = conn.sendall(input)

s.close()
exit()
