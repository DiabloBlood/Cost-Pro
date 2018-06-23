import logging



def add_log_1(func, *args, **kwargs):
    result = func(*args, **kwargs)
    logging.warning('%s is running' % func.__name__)
    return result

def foo_1(name):
    print 'I am %s' % name
    return 1

def bar_1(name):
    print 'I am %s' % name
    return 2

# print add_log_1(foo_1, 'foo_1')
# print add_log_1(bar_1, 'bar_1')



def add_log_2(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.warning('%s is running' % func.__name__)
        return result

    return wrapper

def foo_2(name):
    print 'I am %s' % name
    return 1

def bar_2(name):
    print 'I am %s' % name
    return 2

foo_2 = add_log_2(foo_2)
bar_2 = add_log_2(bar_2)

# print foo_2('foo_2')
# print bar_2('bar_2')


'''
def add_log_3(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.warning('%s is running' % func.__name__)
        return result

    return wrapper

@add_log_3
def foo_3(name):
    print 'I am %s' % name
    return 1

@add_log_3
def bar_3(name):
    print 'I am %s' % name
    return 2

# print foo_3('foo_3')
# print bar_3('bar_3')
'''


'''
def add_log_4(level='debug'):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if level == 'warning':
                logging.warning('%s is running' % func.__name__)
            return result

        return wrapper

    return decorator



@add_log_4(level='warning')
def foo_4(name):
    print 'I am %s' % name
    return 1

def bar_4(name):
    print 'I am %s' % name
    return 2

print foo_4('foo_4')
print bar_4('bar_4')
'''

import sys

def add_log_3(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.warning('%s is running' % func.__name__)
        return result

    return wrapper


def foo_3(name):
    frame = sys._getframe()
    print frame.f_code.co_name
    print frame.f_back.f_code.co_name
    print 'I am %s' % name
    return 1

'''
@add_log_3(foo_3)
def bar_3(name):
    print 'I am %s' % name
    return 2
'''

def bar_3(name):
    print 'I am %s' % name
    return 2
temp = add_log_3(foo_3)
print temp(bar_3)
# bar_3 = temp(bar_3)

# print foo_3('foo_3')
# print bar_3('bar_3')
print bar_3