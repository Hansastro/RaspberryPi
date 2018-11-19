#!/usr/bin/python           # This is server.py file                                                                                                                                                                           

import socket               # Import socket module
import _thread

def on_new_client(clientsocket,addr):
    msg = clientsocket.recv(1024)
    print('Get message from', msg.decode("utf-8"), '-->', addr[0])
    clientsocket.close()

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = '192.168.2.76'
port = 5001                 # Reserve a port for your service.

print('Server started!')
print('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.


while True:
   c, addr = s.accept()     # Establish connection with client.
   _thread.start_new_thread(on_new_client,(c,addr))

s.close()
