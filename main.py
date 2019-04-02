import register
from threading import Thread
import login
import database
import fileManager
from interface import *
from server import *
from time import sleep

def login_user(s):
    send_info(s,"L")

def register_user(s):
    send_info(s,"R")

def start_user_session(s):
    menu = "\n"
    menu += "1) Login\n"
    menu += "2) Register\n"
    menu += "3) Exit\n"
    menu += ">"
    opt = int(get_input(s,menu))
    if(opt == 1):
        login_user(s)
    if(opt == 2):
        register_user(s)
    if(opt == 3):
        pass

def client_handler(client,addr):
    print("[*] Connection from %s"%(str(addr[0])))
    send_message(client,"Welcome to Data Storzz")
    start_user_session(client)

def main():
    print("[*] Starting Server")
    sleep(1)
    print("[*] Server Started")
    while True:
        client,addr = start_server()
        thread = Thread(target=client_handler,args=(client,addr,))
        thread.start()


if __name__ == '__main__':
    main()
