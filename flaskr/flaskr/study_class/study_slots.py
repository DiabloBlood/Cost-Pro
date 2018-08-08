import sys
sys.path.append('/var/www/report/zcur/flaskr/flaskr/')
from util.util import show_descr, is_descr



# 0. Access __slots__
class A(object):
    __slots__ = ('a', 'b')
t = A()

# 0.(1). instance and class all could access
assert t.__slots__ == A.__slots__
assert id(t.__slots__) == id(A.__slots__)   # same reference
assert isinstance(t.__slots__, tuple) and isinstance(A.__slots__, tuple)
assert cmp(t.__slots__, ('a', 'b')) == 0
assert cmp(A.__slots__, ('a', 'b')) == 0
# 0.(2). __slots__ is not descriptor, only tuple or list
assert not is_descr(t.__slots__)
assert not is_descr(A.__slots__)

class A(object):
    __slots__ = ['a', 'b']
t = A()
# 0.(3). instance and class all could access
assert t.__slots__ == A.__slots__
assert id(t.__slots__) == id(A.__slots__)   # same reference
assert isinstance(t.__slots__, list) and isinstance(A.__slots__, list)
assert cmp(t.__slots__, ['a', 'b']) == 0    # this class __slot__ defined by a list instead of tuple
assert cmp(A.__slots__, ['a', 'b']) == 0
# 0.(4). __slots__ is not descriptor, only tuple or list
assert not is_descr(t.__slots__)
assert not is_descr(A.__slots__)



# 1. If __solts__ defined, instance doesn't has '__dict__' and '__weakref__'
class A(object):
    __slots__ = ('a', 'b')

t = A()
assert '__dict__' not in dir(t) and '__weakref__' not in dir(t)
# 1.(1) class also doesn't has '__dict__' and '__weakref__'
assert '__dict__' not in dir(A) and '__weakref__' not in dir(A)



# 2. Instance attempts to assgin to an unlisted variable name will raises AttributeError
try:
    t.c = 5
except AttributeError:
    pass



# 3. If dynamic assignment of new variables is desired, then add '__dict__' to __slots__.
class A(object):
    __slots__ = ('a', 'b', '__dict__')

t = A()
assert '__dict__' in dir(t)
t.c = 5     # No exceptions throwed
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
assert is_descr(t.__class__.a) is False

# 7.
class A(object):
    __slots__ = ('a', 'b')

class B(A):
    pass

class C(B):
    pass

t = B()
# 7.(1). '__dict__' and '__weakref__ in subclass if superclass defined __slots__
assert '__dict__' in dir(B)
assert '__weakref__' in dir(B)
# 7.(2). if subclass not define __slots__, it will inherits from superclass
assert cmp(B.__slots__, ('a', 'b')) == 0
assert cmp(C.__slots__, ('a', 'b')) == 0

# 7.(3). instance still has '__dict__' and '__weakref__' if instance.__class__ not define __slots__
assert '__dict__' in dir(t) and '__weakref__' in dir(t)


class A(object):
    __slots__ = ('a', 'b')

class B(A):
    __slots__ = ('c', 'd')

class C(B):
    pass

t = B()
t2 = C()
# 7.(4). if subclass not define __slots__, if will inherits the nearest superclass's __slots__
assert cmp(C.__slots__, ('c', 'd')) == 0
assert cmp(t.__slots__, ('c', 'd')) == 0
assert cmp(t2.__slots__, ('c', 'd')) == 0

