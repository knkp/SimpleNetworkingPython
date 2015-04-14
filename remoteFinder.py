import socket


class RemoteFinder:

    #locally assigned name

    friendlyName = ''

    #server metadata
    sizeOfMessage = 1
    msgSendingLocalAddress = b's'
    msgRequestRemoteAddress = b'r'
    ack = ''

    server_address_ip = ''
    server_port = ''
    sock = ''
    remoteAddress_ip = ''
    remoteAddress_port = ''
    local_address = ''


    def __init__(self, friendlyName, awsServerIP, awsServerPort):
        self.friendlyName = friendlyName
        self.server_address_ip = awsServerIP
        self.server_port = awsServerPort
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.local_address = socket.gethostbyname(socket.gethostname())
        self.server_address = (self.server_address_ip, self.server_port)
        self.local_address = self.local_address.encode('latin-1') #convert to byte string
        print('connecting to ip address ' + self.server_address_ip + ' port ', self.server_port)


## can now negotiate connection, now need to add friendly name to tranmission as well so that local machine can be resolved

    def uploadLocalAddressToAWS(self):
        lengthlist = []
        self.sock.connect(self.server_address)
        length = len(self.local_address)
        lengthlist.append(length)
        length_bytes = bytes(lengthlist)
        #let aws server know we are sending the local address
        self.sock.sendall(self.msgSendingLocalAddress)
        self.ack = self.sock.recv(3)
        if self.ack == b'ack':
            self.ack = ''
            # send the length of the address to the server
            self.sock.sendall(length_bytes)
            self.ack = self.sock.recv(3)
            if self.ack == b'ack':
                self.ack = ''
                #send the local address
                self.sock.sendall(self.local_address)
                self.ack = self.sock.recv(3)
                if self.ack == b'ack':
                    #yay it worked, moving on
                    print('succesfully updated master server')
                else:
                    print('failed to get ack while uploading local address')
            else:
                print('failed to get ack while uploading local address length')
        else:
            print('failed to get ack while sending sending-local-address request')

        self.sock.close()

    def getRemoteAddress(self):
        self.sock.connect(self.server_address)


    def connectToRemoteAddress(self):
        self.sock.connect(self.server_address)

    def closeRemoteAddress(self):
        print('closing remote address port')
        self.sock.close()
