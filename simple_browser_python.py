import socket
#Make the socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Phone call to socket
mysock.connect(('data.pr4e.org', 80))
#Whatever command - convert to UTF-8
cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r".encode()
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if len(data) < 1:
		break
	#Convert UTF-8 to unicode and print 
	print(data.decode(), end = '')

mysock.close()