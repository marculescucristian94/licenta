#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import time

queue_dict = {}
#current_ticket = 0
#most_recent = 0

s = socket.socket()         # Create a socket object
host = 'localhost'          # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
pending_clients = []

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   '''
   if not addr[0] in queue_dict:
      queue_dict[addr[0]] = most_recent
      most_recent += 1
   print queue_dict
   '''
   if not addr[0] in pending_clients:
      pending_clients.append(addr[0])
   print pending_clients
   if pending_clients[0] == addr[0]:
      response = 'ACK'
   else:
      response = 'NACK'
   #response = 'Current ticket: ' + str(current_ticket) + ', Your ticket: ' + str(queue_dict[addr[0]])   
   print 'Got connection from', addr
   c.send(response)
   c.close()                # Close the connection
