import logging
import sys
import SocketServer

# logging.basicConfig(format='%(name)s: %(message)s', level=logging.DEBUG)

if __name__ == '__main__':
    logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(name)s: %(message)s')
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')