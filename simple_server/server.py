import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('10.0.2.15', 8001)

print >> sys.stderr, 'starting up on %s port %s' % server_addr

sock.bind(server_addr)

sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()