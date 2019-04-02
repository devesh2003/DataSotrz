import socket
from interface import *
from time import sleep
import sys

def login(s):
    print("L")

def register(s):
    print("R")

def start_session(s):
    send_input(s)
    m = get_info(s)
    if(m == 'L'):
        login(s)
    elif(m == 'R'):
        register(s)
    else:
        print("[*] Invalid option received.....\n [*] Exiting...")
        sys.exit(1)

def main():
    ip = "127.0.0.1"
    port = 2003
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((str(ip),int(port)))
    get_message(s)
    start_session(s)

if __name__ == '__main__':
    main()
