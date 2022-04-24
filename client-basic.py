#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Author : Ayesha S. Dina

import os
import sys
import socket
import ipaddress



IP = "localhost"
PORT = 4451
ADDR = (IP,PORT)
SIZE = 1024 ## byte .. buffer size
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"
    
def main():
    while True:
        #get command, only "CONNECT" or "HALT" allowed.
        data = input("> ")
        data = data.split(" ")
        cmd = data[0]
        if cmd.upper() == "CONNECT":
            addr = (data[1],int(data[2]))
            client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.connect(addr)
        elif cmd.upper() == "HALT":
            sys.exit()
        else:
            print('Command not recognized. No server connected, options are "CONNECT server_ip server_port" or "HALT"')
        #post-connection command handler
        while True:  ### multiple communications
            data = client.recv(SIZE).decode(FORMAT)
            cmd, msg = data.split("@")
            if cmd == "OK":
                print(f"{msg}")
            elif cmd == "DISCONNECTED":
                print(f"{msg}")
                break
            
            data = input("> ") 
            data = data.split(" ")
            cmd = data[0]
            if cmd.startswith("CONNECT"):
                if data.len() == 3:
                    addr = (data[1],data[2])
                    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    client.connect(addr)
            if cmd == "CREATE":
                client.send(cmd.encode(FORMAT))

            elif cmd == "LOGOUT":
                client.send(cmd.encode(FORMAT))
                break
            elif cmd == "HALT":
                client.send(cmd.encode(FORMAT))
                break
            elif cmd == "UPLOAD":
                client.send(cmd.encode(FORMAT))
            elif cmd == "DOWNLOAD":
                client.send(cmd.encode(FORMAT))
            elif cmd == "DIR":
                client.send(cmd.encode(FORMAT))



    print("Disconnected from the server.")
    client.close() ## close the connection

if __name__ == "__main__":
    main()