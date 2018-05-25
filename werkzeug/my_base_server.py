

import threading


class MyBaseServer(object):
    def __init__(self, server_address, RequestHandlerClass):
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.__is_shut_down = threading.Event()
        print dir(self.__is_shut_down)


if __name__ == '__main__':
    MyBaseServer(1, 2)