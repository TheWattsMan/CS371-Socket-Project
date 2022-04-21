#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Author : Ayesha S. Dina

import os
import socket
import threading
import subprocess

# IP =  "192.168.1.101" #"localhost"
IP = "localhost"
PORT = 4451
ADDR = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_PATH = "server"

#File creation
path = './'
fileName = 'Simple-text-file.txt'
buff = "ABCD \n"

### to handle the clients
def handle_client (conn,addr):


    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("OK@Welcome to the server".encode(FORMAT))

    while True:
        data =  conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]
       
        send_data = "OK@"

        if cmd == "LOGOUT":
            break

        elif cmd == "CREATE": 
            with open(os.path.join(path,fileName), 'w') as temp_file: ##### creating the file
                temp_file.write(buff)
            send_data += "file " + path + fileName + " created."

            conn.send(send_data.encode(FORMAT))
        elif cmd == "HALT":
            quit()
        elif cmd == "UPLOAD":
            send_data += "File " + path + fileName + " uploaded."
            conn.send(send_data.encode(FORMAT))
        elif cmd == "DOWNLOAD":
            send_data += "File " + path + fileName + " downloaded."
            conn.send(send_data.encode(FORMAT))
        elif cmd == "DIR":
            lsComm = "ls " + path
            lsOut = subprocess.check_output(lsComm)
            send_data += "LS response: " + lsOut.decode("utf-8")
            conn.send(send_data.encode(FORMAT))



    print(f"{addr} disconnected")
    conn.close()


def main():
    print("Starting the server")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) ## used IPV4 and TCP connection
    server.bind(ADDR) # bind the address
    server.listen() ## start listening
    print(f"server is listening on {IP}: {PORT}")
    while True:
        conn, addr = server.accept() ### accept a connection from a client
        thread = threading.Thread(target = handle_client, args = (conn, addr)) ## assigning a thread for each client
        thread.start()


if __name__ == "__main__":
    main()

