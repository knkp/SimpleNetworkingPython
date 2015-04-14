import masterServer

server = masterServer.MasterServer('127.0.0.1', 5001)
server.SETUP_SERVER()
while 1:
    server.SERVICE_REQUEST()