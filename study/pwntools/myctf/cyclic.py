from pwn import *

# context.arch = "amd64"
# context.os = "linux"
# context.endian = "little"
# context.word_size = 64
# when not running on a remote server, its recommended to
context.binary = "./server"

bin = ELF("./server")
srv = process("./server")

stdout = srv.recvline()
print(">" + " &buff1 = " + stdout.decode().split()[-1])
buff1 = int(stdout.decode().split()[-1], 16)

stdout = srv.recvline()
print(">" + " &b = " + stdout.decode().split()[1])
b = int(stdout.decode().split()[1], 16)

srv.sendline(cyclic(512))
print(srv.recv().decode())
print(srv.recvall().decode())
# to get the core, you want to do
# echo core > /proc/sys/kernel/core_pattern
# by analyzing the core with
# gdb server core.47007
# info locals
# we can see that it crashes at b = 0x6161616c
print(cyclic_find(0x6161616C))
# and this does infact give us the correct offset i
# calculated manually
