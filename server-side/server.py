#!/usr/bin/python

import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

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
         command = c.recv(1024)
	 if   command == 'register':
	 	print 'Got register request'
	 elif command == 'autocomplete':
		print 'Got autocomplete request'
	 elif command == 'add_fields':
		print 'Got field add request'      
         c.close()
