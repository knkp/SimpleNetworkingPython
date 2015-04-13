import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = ('',5001)
sock.bind(server_address)
sock.listen(1)

while True:
		print('waiting for a connection')
		connection, client_address = sock.accept()

		try:
				print('connection from', client_address)

				while True:
						data = connection.recv(16)
						print('received %s', data)

						if data:
								print('sending data back to the client')
								connection.sendall(data)
						else:
								print('no more data from client')
								break

		finally:
				connection.close()
