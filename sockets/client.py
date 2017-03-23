#!/usr/bin/python

import socket

s = socket.socket()
# Get IP address of fingerpi
host_port = socket.getaddrinfo('fingerpi.local', 12345)[0][4] 

s.connect(host_port)
print s.recv(1024)
s.close