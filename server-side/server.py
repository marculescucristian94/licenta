#!/usr/bin/python

import socket, fcntl, struct
from register import register_service as rs
from identify import identification_service as iden_s
from database import db_layer

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def register(data):
	id = rs.enrollFingerprint()
	db_layer.db_insert(id, data)
	return id

def autocomplete(id):
	if iden_s.MatchID(id):
		return db_layer.db_select(id)
	else:
		return 'mismatch'

def add_fields(id, data):
	if iden_s.MatchID(id):
		db_layer.db_insert(id, data) 
		return 'ACK'
	else:
		return 'NACK'

if __name__ == '__main__':
   s = socket.socket()
   # For eth0 interface
   host = get_ip_address('eth0')
   # For wlan0 interface
   #host = get_ip_address('wlan0')
   print host
   port = 6000                 # Reserve a port for your service.
   s.bind((host, port))         # Bind to the port
   pending_clients = []

   s.listen(5)
   while True:
      c, addr = s.accept()
      if not addr[0] in pending_clients:
         pending_clients.append(addr[0])
      print 'Got connection from', addr
      print pending_clients
      if not pending_clients[0] == addr[0]:
         response = 'NACK'
         c.send(response)
         c.close()
      else:
         response = 'ACK'
         c.send(response)
	 request = c.recv(1024)
         command = request.split('*')[0]
	 #data = request.split('*')[1]
	 if   command == 'register':
	 	print 'Got register request'
		data = request.split('*')[1]
		print 'Got data: ', data
		response = str(register(data))
		c.send(response)
	 elif command == 'autocomplete':
		print 'Got autocomplete request'
		id = int(request.split('*')[1])
		print 'Got id: ', id
		response = autocomplete(id)
		print response
		c.send(response)
	 elif command == 'add_fields':
		print 'Got field add request'
		id = int(request.split('*')[1])
		print 'Got id: ', id
		data = request.split('*')[2]
		print 'Got data: ', data
		response = add_fields(id, data)
		c.send(response)      
         c.close()
