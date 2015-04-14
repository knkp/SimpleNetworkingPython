__author__ = 'Stephen'

import socket

class MasterServer:


    #server metadata

    REQUEST = ''
    sizeOfMessage = 1
    REQUEST_sending_local_address = b's'
    REQUEST_remote_address = b'r'
    ack = b'ack'

    # endpoint addresses
    addressList = []

    # tcp stuff
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ()

    def __init__(self, serverAddress, port):
        self.server_address = (serverAddress, port)


    def SETUP_SERVER(self):
        self.sock.bind(self.server_address)
        self.sock.listen(5)


    def SERVICE_REQUEST(self):

        while True:
            print('waiting for a connection')
            self.connection, client_address = self.sock.accept()
            print('connection from', client_address)

            while True:
               self.REQUEST = self.connection.recv(self.sizeOfMessage)
              # print(self.REQUEST)
               if len(self.REQUEST) > 0:

                   self.sendACK()

                   if self.REQUEST == self.REQUEST_sending_local_address:
                       print('getting remote address')
                       localAddress = self.receiveLocalAddress()
                       print(localAddress)
                       if localAddress == -1:
                           print('something went wrong')
                           return
                       else:
                           self.addressList.append(localAddress)
                           return

                   elif self.REQUEST == self.REQUEST_remote_address:
                       print('sending address')
                   else:
                       print('error non-identifiable request')


    def receiveLocalAddress(self):
        print('recording address')

        lengthBytes = self.connection.recv(2)

        if len(lengthBytes) > 0:
            length = int.from_bytes(lengthBytes, 'little')
            self.sendACK()
            uploadedAddress = self.connection.recv(length)

            if len(uploadedAddress) > 0:
                self.sendACK()
            else:
                print('failed to retrieve address')
                return -1
        else:
            print('failed to get length of address')
            return -1

        return uploadedAddress


    def transmitRemoteAddress(self):
        print('sending address')

    def sendACK(self):
        print('sending ack')
        self.connection.sendall(self.ack)