import socket

PORT = 6969 #choose a port. must be same on client and server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', PORT))
s.listen(5)
client,addr=s.accept()
print client.recv(1024)
while True:
	client.send(raw_input('> '))
	print client.recv(4096)
	

	
