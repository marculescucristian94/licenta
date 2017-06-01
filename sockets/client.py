#!/usr/bin/python

import socket

s = socket.socket()
# mDNS version
server_info = socket.getaddrinfo('fingerpi.local', 6000)[0][4]
print server_info
host = server_info[0]
port = server_info[1]
s.connect((host, port))

# Hard-coded IP address
'''
host = 'localhost'
port = 12345
s.connect((host, port))
'''

print s.recv(1024)
request = 'client request'
s.sendall(request)
s.close()
