import socket
from datetime import datetime

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"Scanning target: {target}")
        print(f"Time started: {datetime.now()}")

        for port in range(0,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.05)

            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port}: open")
    except:
        s.close()
        print("failed")
        exit()
    print(f"Time ended: {datetime.now()}")

target = input("Enter IP addr: ")
port_scan(target)
