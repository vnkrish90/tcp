import socket

def Main():
    host = "192.168.1.6"
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = input("-> ")
    while message != 'q':
        fmessage = message.encode()
        s.send(fmessage)
        data = s.recv(1024)
        print('Received from server: ' + str(data))
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    Main()
