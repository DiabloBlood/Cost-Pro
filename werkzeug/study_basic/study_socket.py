import socket


# host = '10.0.2.15'
host = '10.0.2.15'
port = 8001

addr = (host, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(addr)

server.listen(1)

while True:
    print('Server serve on address {}'.format(server.getsockname()))
    conn, addr = server.accept()
