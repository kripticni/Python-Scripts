import paramiko
from getpass import getpass
import time

host = input("Host - ")
user = input("User - ")
passwd = input("Password - ")

session = paramiko.SSHClient()
private_key = paramiko.RSAKey.from_private_key_file('id_rsa')
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#session.set_missing_host_key_policy(paramiko.RejectPolicy())
#session.set_missing_host_key_policy(paramiko.WarningPolicy())

session.connect(hostname=host,
                username=user,
                password=passwd,
                pkey=private_key)

commands = ["pwd", "cd ~", "ls","echo $USER","hostname"]

for cmd in commands:
    print("$", cmd)
    stdin,stdout,stderr = session.exec_command(cmd)
    print(str(stdout.read().decode('utf-8').strip()))
    print(str(stderr.read().decode('utf-8').strip()))
