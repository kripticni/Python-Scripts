from pwn import *

context.arch = "amd64"
context.os = "linux"
context.endian = "little"
context.word_size = 64
# context.log_level = "debug" useful for debugging

srv = process("./server")
# works with remote, listen, ssh also
stdout = srv.recvline()

# instruction = enhex(asm("mov eax,0"))
# print(disasm(unhex(instruction)))

e = ELF("./server")
print(hex(e.address))
print(e.symbols)
print(e.got)
print(e.plt)
