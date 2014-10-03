import socket

PORT = 6969 #choose a port. must be same on client and server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', PORT))
s.listen(5)
client,addr=s.accept()
print client.recv(1024)
while True:
	command = raw_input('> ')
	if command != '':
		try:
			client.send(command)
			print client.recv(4096)
		except socket.error:
			print ('Error')
			client,addr=s.accept()