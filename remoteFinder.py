class remoteFinder:
	def __init__(self,awsServerIP,awsServerPort):
		self.server_address_ip = awsServerIP
		self.server_port = awsServerPort
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.local_address = socket.gethostbyname(socket.gethostname())
		self.server_address = (self.server_address_ip, self.server_port)

		print('connecting to ip address ' + self.server_address_ip + ' port ', self.server_port)

		sock.connect(self.server_address)

	def uploadAddress:

	def getRemoteAddress:

	def connectToRemoteAddress:

	def connectToAwsServer:

	def closeConnection:
		
