# Client
import socket
sock = socket.socket()
sock.connect(("localhost", 2042))
my_username = input("Your name: ")

while True:
    message = input(f"{my_username}> ")
    if message:
        message = message.encode('utf-8')
        sock.send(message)

    while True:



data = sock.recv(1024)
sock.close()
print(data)