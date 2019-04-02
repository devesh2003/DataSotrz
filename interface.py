import socket
from time import sleep
#global variables
size = 1000

def get_info(s,size=1000):
    info = s.recv(size).decode()
    return info

def send_info(s,info):
    s.send(info.encode())
    return

def send_message(s,msg):
    s.send(msg.encode())
    return

def get_message(s,size=1000):
    msg = s.recv(size).decode()
    print(msg)
    return

def get_input(s,msg):
    global size
    s.send(msg.encode())
    sleep(1)
    output = s.recv(size).decode()
    return output

def send_input(s):
    global size
    msg = s.recv(size).decode()
    sleep(1)
    data = str(input(msg))
    s.send(data.encode())
    return
