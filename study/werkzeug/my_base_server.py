

import threading


class MyBaseServer(object):
    def __init__(self, server_address, RequestHandlerClass):
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.__is_shut_down = threading.Event()
        self.__shutdown_request = False
        print dir(self.__is_shut_down)


if __name__ == '__main__':
    MyBaseServer(1, 2)