import socket



HOST = '10.0.2.15'
PORT = 8001

def create_client(count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_addr = (HOST, PORT)

    print 'connecting to HOST: {} PORT: {}'.format(HOST, PORT)
    client.connect(server_addr)

    try:
        msg = 'ABCDEFGHI{}'.format(count)
        print 'sending message [{}]'.format(msg)
        client.sendall(msg)
    finally:
        print 'closing client socket......'
        client.close()

count = 1
while True:
    create_client(count)
    count += 1
    if count > 100:
        break