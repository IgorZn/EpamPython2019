import sys
import socket
import threading

class Server:
    IP = '127.0.0.1'    # IP на котором будет работать сервер
    PORT = 2042         # порт для сервера
    HEADER_LENGTH = 1024    # длина сообщения (макс)

    sock = socket.socket() # назначаем сокет
    connections = [] # список адресов клиентов

    def __init__(self):
        self.sock.bind((self.IP, self.PORT))    # запускаем сокет на ИП и порт
        self.sock.listen(1)     # количество подключений

    def handler(self, conn, addr):
        """
        принимает соединения и обрабатывает соедения
        :param conn:
        :param addr:
        :return:
        """
        while True:
            data = conn.recv(self.HEADER_LENGTH)    # message
            for connection in self.connections:     # send data to all in connections
                connection.send(data)
            if not data:    # shutdown server if NO data
                print(str(addr[0]) + ':' + str(addr[1]) + ' disconnected')
                self.connections.remove(conn)
                conn.close()
                break

    def run(self):
        """
        run server in Thread
        :return:
        """
        while True:
            conn, addr = self.sock.accept() # ожидать соединения с клиентом
            serverThread = threading.Thread(target=self.handler, args=(conn, addr))
            serverThread.daemon = True
            serverThread.start()
            self.connections.append(conn)
            print(str(addr[0]) + ':' + str(addr[1]) + ' connected')

class Client:
    sock = socket.socket()

    def send_message(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))

    def __init__(self, addr='127.0.0.1'):
        self.sock.connect((addr, 2042))

        clientThread = threading.Thread(target=self.send_message)
        clientThread.daemon = True
        clientThread.start()

        while True:
            data = self.sock.recv(1024)
            if data == bytes("{quit}", "utf8"):
                self.sock.close()
                break
            print(str(data, 'utf-8'))

if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        if sys.argv[1] == 'client':
            client = Client()
        else:
            client = Client(sys.argv[1])
    else:
        print("Waiting for connection...")
        server = Server()
        server.run()


# cd 07-networks-basics
# python 07_socket.py client
# cd 07-networks-basics && python 07_socket.py client