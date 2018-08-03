import sys
sys.path.append('/var/www/report/zcur/flaskr/flaskr/')
from util.util import show_descr



# 1. If __solts__ define, instance doesn't have '__dict__' and '__weakref__'
class A(object):
    __slots__ = ('a', 'b')

t = A()
assert '__dict__' not in dir(t) and '__weakref__' not in dir(t)



# 2. Instance attempts to assgin to an unlisted variable name raises AttributeError
try:
    t.c = 5
except AttributeError:
    pass



# 3. If dynamic assignment of new variables is desired, then add '__dict__' to __slots__.
class A(object):
    __slots__ = ('a', 'b', '__dict__')

t = A()
assert '__dict__' in dir(t)
print show_descr(t.__dict__)
t.c = 5
assert t.__dict__['c'] == 5

# 4. If want '__weakref__', then add to __slots__.
class A(object):
    __slots__ = ('a', 'b', '__weakref__')

t = A()
assert '__weakref__' in dir(t)