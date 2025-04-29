from pwn import *

# io = process(["./echo-process.py", "arg"])
io = remote("0.0.0.0", 51256)
# also you can specify the type and familiy
# of the connection with fam='...' and typ='...'

# SSH is crazy well made too, probably a complete substitute for paramiko?
# session = ssh('bandit0', 'bandit.labs.overthewire.org', 2220, password='bandit0')
# io = session.process('/bin/sh', env={"PS1":""})

io.send(b"first input")
out = io.recv()
print(out.decode())

# io.interactive() this never returns, but its pretty useful regardless

while True:
    cmd = input("$ ").encode()
    if cmd.strip() == b"exitpwninteractive":
        break
    io.sendline(cmd)
    print(io.recv().decode())
