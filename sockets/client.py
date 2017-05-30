#!/usr/bin/python

import socket

s = socket.socket()
# Get IP address of fingerpi, works on Linux
host_port = socket.getaddrinfo('fingerpi.local', 12345)[0][4]
print host_port

# Get IP address of fingerpi, works on Windows
#host = 'localhost'
#port = 12345

# Connect from Linux client
s.connect(host_port)

# Connect from Windows client
#s.connect((host, port))
print s.recv(1024)
s.close
