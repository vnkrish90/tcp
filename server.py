import socket
import time

#Create a Socket object

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket Created")
 
#Get Local Machine Name

host = socket.gethostname()

port = 9999

print("Socket bind Completed")

#bind the host to port

serversocket.bind((host, port))

#Queue upto 5 Parallel Requests

serversocket.listen(5)

print("Socket now listening")

while True:
	#Establish a Connection
	clientsocket,addr = serversocket.accept()

	print("Got a Connection from %s" % str(addr))
	currentTime = time.ctime(time.time()) + "\r\n"
	clientsocket.send(currentTime.encode('ascii'))
	clientsocket.close()
