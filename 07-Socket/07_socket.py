# Server
import socket
IP = '127.0.0.1'
PORT = 2042
HEADER_LENGTH = 1024

sock = socket.socket()
sock.bind((IP, PORT))

sock.listen(1)

conn, addr = sock.accept()
while True:
    name = conn.recv(HEADER_LENGTH)
    if not name:
        break
    conn.send(f"Hello, dear {name}".encode('utf-8'))

conn.close()
