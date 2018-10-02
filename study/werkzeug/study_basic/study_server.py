# BaseSelector
# +-- SelectSelector
# +-- PollSelector
# +-- EpollSelector
# +-- DevpollSelector
# +-- KqueueSelector

# Constant    Meaning
# EVENT_READ  Available for read
# EVENT_WRITE Available for write

import select
import socket
import time


# readers = set()
# writers = set()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '10.0.2.15'
port = 8001

server.bind((host, port))

server.listen(5)

import sys
print(sys.stdin.fileno())
print(sys.stdout.fileno())
print(sys.stderr.fileno())
print(server.fileno())

readers = [server]
writers = []
errors = []


try:
    while True:
        r, w, err = select.select(readers, writers, errors)
        print(r, w)
        for fd in r:
            if fd == server:
                print(fd)
        time.sleep(2)
finally:
    server.close()