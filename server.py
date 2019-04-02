import socket
import sys
import struct

def udp_server(port):
    pass

def start_server(port=2003,ip="127.0.0.1",protocol="TCP"):
    if(protocol == "UDP"):
        #UDP SERVER(BETA)
        udp_server(port)
        return
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((str(ip),int(port)))
    #print("[*] Server Binded")
    s.listen(5)
    client,addr = s.accept()
    return client,addr
