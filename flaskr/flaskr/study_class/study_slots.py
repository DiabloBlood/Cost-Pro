import sys
sys.path.append('/var/www/report/zcur/flaskr/flaskr/')
from util.util import show_descr, is_descr



# 0. Access __slots__
class A(object):
    __slots__ = ('a', 'b')
t = A()

# instance and class all could access
assert t.__slots__ == A.__slots__
assert id(t.__slots__) == id(A.__slots__)
assert isinstance(t.__slots__, tuple) and isinstance(A.__slots__, tuple)
assert cmp(t.__slots__, ('a', 'b')) == 0
assert cmp(A.__slots__, ('a', 'b')) == 0
# __slots__ is not descriptor, only tuple or list
assert not is_descr(t.__slots__)
assert not is_descr(A.__slots__)

class A(object):
    __slots__ = ['a', 'b']
t = A()
# instance and class all could access
assert t.__slots__ == A.__slots__
assert id(t.__slots__) == id(A.__slots__)
assert isinstance(t.__slots__, list) and isinstance(A.__slots__, list)
assert cmp(t.__slots__, ['a', 'b']) == 0
assert cmp(A.__slots__, ['a', 'b']) == 0
# __slots__ is not descriptor, only tuple or list
assert not is_descr(t.__slots__)
assert not is_descr(A.__slots__)



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
t.c = 5
assert t.__dict__['c'] == 5

# 4. If want '__weakref__', then add to __slots__.
class A(object):
    __slots__ = ('a', 'b', '__weakref__', '__dict__')

t = A()
assert '__weakref__' in dir(t)


# 5. __slots__ are implemented at the class level by creating descriptors for each variable name.
assert is_descr(t.__class__.a)
assert is_descr(t.__class__.__weakref__)

### Important tips: instance __dict__ and dictproxy all are not descriptors
assert not is_descr(t.__dict__)
assert not is_descr(t.__class__.__dict__)

# 6. As a result, class attributes cannot be used to set default values for instance variables
# defined by __slots__; otherwise, the class attribute would overwrite the descriptor assignment.
class A(object):
    __slots__ = ('a', 'b')
    a = 5

t = A()
assert not is_descr(t.__class__.a)

# 7.
class A(object):
    __slots__ = ('a', 'b')

class B(A):
    pass

t = B()
print t.__slots__
print t.__dict__

class A(object):
    __slots__ = ('a', 'b')

class B(A):
    __slots__ = ('c', 'd')

t = B()
print t.__slots__