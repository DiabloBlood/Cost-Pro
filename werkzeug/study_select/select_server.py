import select
import socket
import sys
import Queue

HOST = '10.0.2.15'
PORT = 8001

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set sockt to non-blocking mode
server.setblocking(0)

# Bind the socket to the port
server_address = (HOST, PORT)
print >>sys.stderr, 'starting up on %s port %s' % server_address
socket.bind(server_address)

# Listen for incoming connections
socket.listen(5)

# sockets from which we expect to read
inputs = [server]
# sockets we expect to write
outputs = []

'''
1. Connections are added to and removed from these 3 lists by the server main loop.
2. Server is going to wait for a socket to become writable before sending any data (instead of immediately sending the reply).
'''

# Outgoing message queues (socket:Queue)
message_queues = {}

while inputs:
    # Wait for at least one of the sockets to be ready for processing
    print >>sys.stderr, '\nwaiting for the next event'
    '''
    1. readable list have incoming data buffered and available to be read.
    2. All of the sockets in the writable list have free space in their buffer and can be written to.
    3. The sockets returned in exceptional have had an error (the actual definition of “exceptional condition” depends on the platform).
    '''
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    # Handle inputs
    for s in readable：
        if s is server:
            # A "readable" server socket is ready to accept a connection
            conn, client_addr = s.accept()
            print >>sys.stderr, 'new connection from ', client_addr
            conn.setblocking(0)
            inputs.append(conn)

            # Give the connection a queue for data we want to send
            message_queues[conn] = Queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data
                print sys.stderr, 'received "%s" from %s' % (data, s.getpeername())
                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else: