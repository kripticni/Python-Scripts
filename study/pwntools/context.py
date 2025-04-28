from pwn import *

context.arch = "adm64"
context.endian = "little"
context.sign = "unsigned"
context.bits = 64
context.log_file = "pwn.log"
context.log_level = "debug"
context.terminal = "alacritty"
context.timeout = 5
