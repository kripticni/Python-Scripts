from getpass import getpass
import paramiko
import time

#bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0
host = "bandit.labs.overthewire.org"
port = 2220
user = "bandit0"
passwd = "bandit0"

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(hostname=host,
                port=port,
                username=user,
                password=passwd)

stdin, stdout, stderr = session.exec_command('cat readme')
print(stdout.read().decode())
