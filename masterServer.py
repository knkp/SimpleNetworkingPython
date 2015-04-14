__author__ = 'Stephen'

import socket

class MasterServer:

    #server metadata

    REQUEST = ''
    sizeOfMessage = 1
    REQUEST_sending_local_address = b's'
    REQUEST_remote_address = b'r'
    ack = 'ack'

    # endpoint addresses
    addressList = []

    # tcp stuff
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, port):
        server_address = ('', port)
        self.sock.bind(server_address)
        self.sock.listen(1)

        while True:
            print('waiting for a connection')
            self.connection, client_address = self.sock.accept()
            print('connection from', client_address)

            while True:
               self.REQUEST = connection.recv(self.sizeOfMessage)

               if len(self.REQUEST) > 0:
                    if self.REQUEST == self.REQUEST_sending_local_address:
                        print('getting remote address')
                        self.addressList.append(self.receiveLocalAddress())

                    elif self.REQUEST == self.REQUEST_remote_address:
                        print('sending address')
                    else:
                        print('error non-identifiable request')

    def receiveLocalAddress(self):
        print('recording address')
        uploadedAddress = ''

        return uploadedAddress


    def transmitRemoteAddress(self):
        print('sending address')

    def sendACK(self):
