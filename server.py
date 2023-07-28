# this is going to host the connection

import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
PORT = 9999
server.bind((ip, PORT))

server.listen()
print("server is listening---")

conn , address = server.accept()

done = False

while not done:
    message = conn.recv(1024).decode('utf-8')
    if message == 'quit':
        done = True
    else:
        print("client: ", message)
        conn.send(input("Message: ").encode('utf-8'))
        
    