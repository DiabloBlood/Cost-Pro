import logging
import sys
import SocketServer



logging.basicConfig(format='%(name)s: %(message)s', level=logging.DEBUG)


class EchoRequestHandler(SocketServer.BaseRequestHandler):

    def __init__(self, request, client_address, server)：
        self.logger = logging.getLogger('EchoRequestHandler')
        self.logger.debug('__init__')
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        return


if __name__ == '__main__':
    logger = logging.getLogger('haha')
    print logger
    logger2 = logging.getLogger('haha')
    print logger2
    logger3 = logging.getLogger('haha2')
    print logger3