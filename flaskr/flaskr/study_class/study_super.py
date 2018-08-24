import sys

v = int(sys.version[0])


class C(object):
    def func(self):
        return 100
c = C()

c.func   # <bound method C.func of <__main__.C object at 0x7f610780b390>>
C.func   # python2: <unbound method C.func>     ### python3 <function C.func at 0x7f1b92d9b6a8>

C.__dict__['func']      # python2: <function func at 0x7f5592580c80>    ### python3 <function C.func at 0x7f5592580c80>
C.func.__get__(c, C)     # <bound method C.func of <__main__.C object at 0x7ff7ae694390>>

assert id(C.__dict__['func'].__get__(None, C)) == id(C.func)
if v == 3:
    assert C.__dict__['func'].__get__(None, C) is C.func
    assert C.__dict__['func'].__get__(None, C) == C.func
if v == 2:
    assert C.__dict__['func'].__get__(None, C) is not C.func    ### in python2 is failed!!!
    assert C.__dict__['func'].__get__(None, C) == C.func

assert id(C.__dict__['func'].__get__(c, C)) == id(c.func)
assert C.__dict__['func'].__get__(c, C) == c.func




### python2 super.__doc__
"""
super(type, obj) -> bound super object; requires isinstance(obj, type)
super(type) -> unbound super object
super(type, type2) -> bound super object; requires issubclass(type2, type)
Typical use to call a cooperative superclass method:
class C(B):
    def meth(self, arg):
        super(C, self).meth(arg)
"""

### python3 super.__doc__
"""
super() -> same as super(__class__, <first argument>)
super(type) -> unbound super object
super(type, obj) -> bound super object; requires isinstance(obj, type)
super(type, type2) -> bound super object; requires issubclass(type2, type)
Typical use to call a cooperative superclass method:
class C(B):
    def meth(self, arg):
        super().meth(arg)
This works for class methods too:
class C(B):
    @classmethod
    def cmeth(cls, arg):
        super().cmeth(arg)
"""


def print_init(obj):
    print('{} init'.format(obj.__class__.__name__))


class A(object):
    def __init__(self):
        print_init(self)


class B(A):
    def __init__(self):
        print_init(self)



# 1. super() only works for new-style classes
# 2. If the second argument is an object, isinstance(obj, type) must be true

try:
    super(B, 5)
except TypeError:
    pass

# t = B()
# super(B, t)     # <super: <class 'B'>, <B object>>
# super(A, t)      # <super: <class 'A'>, <B object>>

class A(object):
    def m(self): print "save A's data"
class B(A):
    def m(self): print "save B's data"; super(B, self).m()
class C(A):
    def m(self): print "save C's data"; super(C, self).m()
class D(B, C):
    def m(self): print "save D's data"; super(D, self).m()

d = D()
# d.m()     # Order is mro: DBCA



class Super(object):

    def __init__(self, obj_type, obj=None):
        self.__type__ = obj_type
        self.__obj__ = obj

    def __get__(self, obj, type=None):
        if self.__obj__ is None and obj is not None:
            return Super(self.__type__, obj)
        else:
            return self

    # proxy use __getattr__ method, since proxy cannot find the corresponding attribute
    def __getattr__(self, attr):
        if isinstance(self.__obj__, self.__type__):
            start_type = self.__obj__.__class__
        else:
            start_type = self.__obj__

        mro = iter(start_type.__mro__)

        for obj_type in mro:
            if obj_type is self.__type__:
                break

        # Note: mro is an iterator, so the second loop
        # picks up where the first one left off!

        for obj_type in mro:
            if attr in obj_type.__dict__:
                x = obj_type.__dict__[attr]
                if hasattr(x, '__get__'):
                    x = x.__get__(self.__obj__)
                return x

        raise AttributeError, attr

    def __repr__(self):
        return '<{}, {}>'.format(self.__type__, self.__obj__)


class A(object):
    def m(self):
        print self
        return 'A'

class B(A):
    def m(self):
        print self
        return 'B' + Super(B, self).m()

class C(A):
    def m(self):
        print self
        return 'C' + Super(C, self).m()

class D(C, B):
    def m(self):
        print self
        return 'D' + Super(D, self).m()

# print D().m() # 'DCBA'
d = D()
# t = Super(D, d)
print d.m()