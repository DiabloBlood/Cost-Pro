import socket
import time



HOST = '127.0.0.1'
PORT = 8001

def create_client(count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_addr = (HOST, PORT)

    print 'connecting to HOST: {} PORT: {}'.format(HOST, PORT)
    client.connect(server_addr)
    print '*****CONNECTED*****{}'.format(count)
    while True:
        time.sleep(100)

    '''
    try:
        client.sendall(str(count))
    except:
        raise
    '''
    # finally:
        # client.close()

count = 1
while True:
    create_client(count)
    count += 1
    if count > 5:
        break