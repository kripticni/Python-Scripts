from pwn import *
import pwnlib.util.hashes
import sys

string = "pwntooling"
char = "p"
num = 1337

print(p32(num))
print(u16(p16(num)))

context.update(endian="little", bits=32)
print(pack(num))

data = read("text.txt")
print("Data from text.txt:", data)
print("Base64 encoded text.txt:", b64e(data))
write("b64text.txt", b64e(data).encode())
print("Url encoded text.txt:", repr(urlencode(data.decode())))
write("urltext.txt", urlencode(data.decode()).encode())

print("Checking both functions by comparing the decode: ", end="")
if urldecode(read("urltext.txt").decode()).encode() == b64d(
    read("b64text.txt").decode()
):
    print("Success!")
else:
    print("Error, something went wrong.")
    sys.exit()

file = "text.txt"
data = read(file)
print("Blake2b for data, then for file:")
print(pwnlib.util.hashes.blake2bfile(file))
print(pwnlib.util.hashes.blake2bsum(data))

print("MD5 for data, then for file:")
print(pwnlib.util.hashes.md5file(file))
print(pwnlib.util.hashes.md5sum(data))

print(f"Hex for '{string}', then bits for '{num}'")
print(enhex(string.encode()))
print(bits(ord(char)))

print("Checking hex functions by comparing the decode: ", end="")
if unhex(enhex(string.encode())) == string.encode():
    print("Success!")
else:
    print("Error, something went wrong.")
    sys.exit()

print("Checking hex functions by comparing the decode: ", end="")
if unbits(bits(ord(char))) == char.encode():
    print("Success!")
else:
    print("Error, something went wrong.")
    sys.exit()

print("Hex dump for 32 bytes of /dev/urandom:")
print(hexdump(read("/dev/urandom", 32)))
