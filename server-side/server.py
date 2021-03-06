#!/usr/bin/python

import socket, fcntl, struct, threading
from register import register_service as rs
from identify import identification_service as iden_s
from database import db_layer
from lcd import I2C_LCD_driver 

RASPRINT_PORT = 6000
MAX_SIZE = 1024
IFNAME = 'eth0'

class ThreadedServer(object):
	def __init__(self):
		self.host = self.get_ip_address(IFNAME)
        	self.port = RASPRINT_PORT
		self.sock = socket.socket()
		self.pending_clients = []
		self.queue_lock = threading.Lock()
		self.lcd = I2C_LCD_driver.lcd()
		self.sock.bind((self.host, self.port))

	def get_ip_address(self, ifname):
    		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    		return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

	def register(self, data):
		id = rs.enrollFingerprint(self.lcd)
		if not id == -1:
			self.lcd.lcd_display_text('Adding info to database...')
			db_layer.db_insert(id, data)
		return id

	def autocomplete(self, id):
		if iden_s.MatchID(id, self.lcd):
			self.lcd.lcd_display_text('Getting info from database...')
			return db_layer.db_select(id)
		else:
			return 'mismatch'

	def add_fields(self, id, data):
		if iden_s.MatchID(id, self.lcd):
			self.lcd.lcd_display_text('Getting info from database...')
			db_layer.db_insert(id, data) 
			return 'success'
		else:
			return 'failure'

	def listen(self):
		self.lcd.lcd_display_text('Awaiting connections...')
		self.sock.listen(10)
		while True:
			client, address = self.sock.accept()
			client.settimeout(60)
			print 'Got connection from', address
			if not address[0] in self.pending_clients:
				self.queue_lock.acquire()
				try:
         				self.pending_clients.append(address[0])
				finally:
					self.queue_lock.release()
			if not self.pending_clients[0] == address[0]:
         			response = 'NACK'
         			client.send(response)
         			client.close()
     			else:
         			response = 'ACK'
         			client.send(response)
				threading.Thread(target = self.solveRequest, args = (client, address)).start()

	def solveRequest(self, client, address):
		request = client.recv(MAX_SIZE)
		command = request.split('*')[0]
		if   command == 'register':
	 		print 'Got register request'
			data = request.split('*')[1]
			print 'Got data: ', data
			response = str(self.register(data))
	 	elif command == 'autocomplete':
			print 'Got autocomplete request'
			id = int(request.split('*')[1])
			print 'Got id: ', id
			response = self.autocomplete(id)
			print response
		elif command == 'add_fields':
			print 'Got field add request'
			id = int(request.split('*')[1])
			print 'Got id: ', id
			data = request.split('*')[2]
			print 'Got data: ', data
			response = self.add_fields(id, data)
		client.send(response)
		self.queue_lock.acquire()
		try:
			self.pending_clients.remove(address[0])
		finally:
			self.queue_lock.release()
		if len(self.pending_clients) == 0:
			self.lcd.lcd_display_text('Awaiting connections...')      
         	client.close()

if __name__ == "__main__":
	ThreadedServer().listen()
	


