# it is said in the documentation
# that when iterating over a bytes
# object, in python3 you get integers
# instead, a better idea is to use
# slices that are of length 1 to
# keep the byte class

from pwn import *

bytes = cyclic(512)

for i in bytes:
    print(i)
# so instead of this, we do

for i in range(len(bytes)):
    print(bytes[i : i + 1])


# also a nice way to demonstrate would be
for i, byte in enumerate(bytes):
    print(byte, bytes[i : i + 1])
