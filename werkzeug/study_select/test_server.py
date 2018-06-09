import socket
import time

HOST = '10.0.2.15'
PORT = 8001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'start server on HOST: {} PORT: {}'.format(HOST, PORT)

server_addr = (HOST, PORT)
server.bind(server_addr)

server.listen(2)

recv_cnt = 0

while True:
    conn, client_addr = server.accept()
    recv_cnt += 1
    try:
        print 'connection from {}'.format(client_addr)
        while True:
            msg = conn.recv(5)
            if msg:
                print 'recv: {} TOTAL: {}'.format(msg, recv_cnt)
            else:
                break;
        time.sleep(100)

    finally:
        print 'close connection from {}'.format(client_addr)
        conn.close()