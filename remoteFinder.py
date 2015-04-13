import socket


class RemoteFinder:


    #server metadata
    sizeOfMessage = 1
    msgSendingLocalAddress = b's'
    msgRequestRemoteAddress = b'r'
    ack = 'ack'

    server_address_ip = ''
    server_port = ''
    sock = ''
    remoteAddress_ip = ''
    remoteAddress_port = ''
    local_address = ''


    def __init__(self, awsServerIP, awsServerPort):
        self.server_address_ip = awsServerIP
        self.server_port = awsServerPort
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.local_address = socket.gethostbyname(socket.gethostname())
        self.server_address = (self.server_address_ip, self.server_port)
        print('connecting to ip address ' + self.server_address_ip + ' port ', self.server_port)


## for this to work correctly, it needs to be able to negotiate with the server on AWS, first, that it is about to transfer
## it's ip address, it then needs to send it the length of the ip address and then the actual ip, strings, ints, etc cannot
## be transferred directly but must be changed into bytes and sent a couple at a time and then reconstructed on the otherside
## This really needs to be finished before anything useful can be done with it - SC 4/13/2015

    def uploadAddressToAWS(self):
        self.sock.connect(self.server_address)
        length = len(self.local_address)
        self.sock.sendall(self.msgSendingLocalAddress)
        self.ack = self.sock.recv(3)
        if self.ack == 'ack':

            self.sock.sendall(self.local_address)

        self.sock.close()

    def getRemoteAddress(self):
        self.sock.connect(self.server_address)


    def connectToRemoteAddress(self):
        self.sock.connect(self.server_address)

    def closeRemoteAddress(self):
