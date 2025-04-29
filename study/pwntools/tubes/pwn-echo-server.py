from pwn import *

client = listen(51256).wait_for_connection()
while True:
    input = client.recv()
    client.send(input)
