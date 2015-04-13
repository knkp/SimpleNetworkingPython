import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_host = socket.gethostname()
server_address = ('52.0.129.208', 5001)
print('connecting to %s port %s',server_address)

sock.connect(server_address)

try:
        message = b'This is a message... for a faggot'
        print('sending %s',message)
        sock.sendall(message)
        amount_received = 0
        amount_expected = len(message)

## need to fix encoding issue, needs to be converted to bytes from int before sent -SC 4/13/2015

        while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print('received %s',data)
finally:
        print('closing socket')
        sock.close()
