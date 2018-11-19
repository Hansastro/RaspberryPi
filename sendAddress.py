#!/usr/bin/python3

import socket
from time import sleep

def client_program():
    hostname = socket.gethostname()  # as both code is running on same pc
    port = 5001  # socket server port number
    host = '192.168.2.76'
    
    cpt = 0
    while cpt <= 5: 
        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server

        message = hostname  # take input

        client_socket.send(message.encode())  # send message
        sleep(5)

        client_socket.close()  # close the connection
        cpt += 1

if __name__ == '__main__':
    sleep(1)
    client_program()
