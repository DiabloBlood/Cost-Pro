import socket
import datetime


# host = '10.0.2.15'
host = '10.0.2.15'
port = 8001

addr = (host, port)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(addr)

# server.listen(1)

while True:
    print('Server serve on address {}'.format(server.getsockname()))
    # conn, addr = server.accept()
    # print('connection from {}'.format(addr))
    msg, addr = server.recvfrom(1024)
    print('connection from {}'.format(addr))

    time = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')

    server.sendto(time.encode(), addr)
    # break

server.close()
