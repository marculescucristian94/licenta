#!/usr/bin/python

import socket

def send_command(request_type, data):
	s = socket.socket()
	# mDNS version
	server_info = socket.getaddrinfo('fingerpi.local', 6000)[0][4]
	print server_info
	host = server_info[0]
	port = server_info[1]
	s.connect((host, port))
	print s.recv(1024)
	request = data
	s.sendall(request)
	s.close()
