import socket


HOST = '10.0.2.15'
PORT = 8001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'start server on HOST: {} PORT: {}'.format(HOST, PORT)

server_addr = (HOST, PORT)
server.bind(server_addr)

server.listen(1)

while True:
    conn, client_addr = server.accept()
    try:
        print 'connection from {}'.format(client_addr)
        while True:
            msg = conn.recv(3)
            if msg:
                print 'server received: {}'.format(msg)
            else:
                a = ''
    finally:
        print 'close connection from {}'.format(client_addr)
        conn.close()