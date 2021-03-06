#!/usr/bin/python

import socket

def send_command(command, data):
	s = socket.socket()
	# mDNS version
	server_info = socket.getaddrinfo('fingerpi.local', 6000)[0][4]
	print server_info
	host = server_info[0]
	port = server_info[1]
	s.connect((host, port))
	print s.recv(1024)
	request = command + '*' + data
	s.sendall(request)
	if command == 'register':
		id = s.recv(1024)
		s.close()
		return id
	elif command == 'autocomplete':
		response = s.recv(1024)
		s.close()
		return response
	elif command == 'add_fields':
		response = s.recv(1024)
		s.close()
		return response
