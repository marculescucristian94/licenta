#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

queue_dict = {}
current_ticket = 0
most_recent = 0

s = socket.socket()         # Create a socket object
host = '192.168.1.110'      # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   if not addr in queue_dict:
      queue_dict[addr] = most_recent
      most_recent += 1
   response = 'Current ticket: ' + str(current_ticket) + ', Your ticket: ' + str(queue_dict[addr])   
   print 'Got connection from', addr
   c.send(response)
   c.close()                # Close the connection
