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

@add_log_4()
def bar_4(name):
    print 'I am %s' % name
    return 2

# print foo_4('foo_4')
# print bar_4('bar_4')



# learn class decorator
class AddLog5(object):

    def __init__(self, func):
        self._func = func

    def __call__(self):
        print 'class decorator running!'
        self._func()
        print 'class decorator ending!'

@AddLog5
def bar_5():
    print 'bar_5'

# bar_5()



from functools import wraps

def my_wraps(func):

    def decorator(wrapper_func):

        def wrapper2(*args, **kwargs):
            return wrapper_func(*args, **kwargs)

        wrapper2.__doc__ = func.__doc__
        wrapper2.__name__ = func.__name__

        return wrapper2

    return decorator

def add_log_6(func):

    # @wraps(func)
    @my_wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.warning('%s is running' % func.__name__)
        return result

    return wrapper

@add_log_6
def foo_6(x):
    """do some math"""
    return x * x

print foo_6.__name__
print foo_6.__doc__

# task: learn partial