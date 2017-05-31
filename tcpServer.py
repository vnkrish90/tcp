import socket

def Main():
    host = ""
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("from connected user: " + str(data))
        data = str(data).upper()
        print("sending: " + str(data))
        byte_message = data.encode()
        c.send(byte_message)
    c.close()

if __name__ == '__main__':
    Main()
