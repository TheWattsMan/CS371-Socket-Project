#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Author : Ayesha S. Dina

import os
import sys
import socket



IP = "localhost"
PORT = 4451
ADDR = (IP,PORT)
SIZE = 1024 ## byte .. buffer size
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"
isConnected = False

def main():
    global isConnected # keeps track of whether connection exists.
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        #get command, only "CONNECT" or "HALT" allowed.
        data = input("> ")
        data = data.split(" ")
        cmd = data[0]
        if cmd.upper() == "CONNECT":
            addr = (data[1],int(data[2]))
            try:
                client.connect(addr)
            except ConnectionRefusedError:
                print("Connection refused. Check your ip/port#")
            except socket.error:
                print("IP/Hostname not found, check IP/Hostname")
            else:
                isConnected = True
        elif cmd.upper() == "HALT":
            sys.exit()
        else:
            print('Command not recognized. No server connected, options are "CONNECT server_ip server_port" or "HALT"')
        #post-connection command handler
        while isConnected:  ### multiple communications
            data = client.recv(SIZE).decode(FORMAT)
            cmd, msg = data.split("@")
            if cmd.upper()  == "OK":
                print(f"{msg}")
            elif cmd.upper()  == "DISCONNECTED":
                print(f"{msg}")
                break
            
            data = input("> ") 
            data = data.split(" ")
            cmd = data[0]
            
            if cmd.upper() == "CREATE":
                client.send(cmd.encode(FORMAT))

            elif cmd.upper()  == "LOGOUT":
                cmd = cmd.upper()
                client.send(cmd.encode(FORMAT))
                client.close()
                isConnected = False
                break
            elif cmd.upper()  == "HALT":
                client.send(cmd.encode(FORMAT))
                break
            elif cmd.upper()  == "UPLOAD":
                client.send(cmd.encode(FORMAT))
            elif cmd.upper()  == "DOWNLOAD":
                client.send(cmd.encode(FORMAT))
            elif cmd.upper()  == "DIR":
                client.send(cmd.encode(FORMAT))
            else:
                print("Command not recognized.")



    print("Disconnected from the server.")
    client.close() ## close the connection

if __name__ == "__main__":
    main()