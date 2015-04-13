import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 5001)
sock.bind(server_address)
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()

    print('connection from', client_address)

    while True:
        data = connection.recv(2)
        if len(data)>0:
            data = int.from_bytes(data, byteorder='little')
            print(data)

# if data:
#			print('sending data back to the client')
#			connection.sendall(data)
#	else:
#			print('no more data from client')
#			break

#	finally:
#			connection.close()
