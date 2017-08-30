import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind to the port
server_name = sys.argv[1]
server_address = (server_name, 10000)
sock.bind(server_address)

#maximum of one connection
sock.listen(1)


while True:
	
	print 'Waiting for a connection'
	
	conn, client_address = sock.accept()
	print 'Connecting from {}'.format(client_address)

	try:
		while True:
			data = conn.recv(16)
			if data:
				print('sending data back to the client')
				conn.sendall(data)
			else:
				print 'no data from', client_address
				break
	finally:
		conn.close()








