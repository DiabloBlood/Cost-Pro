import sys

v = int(sys.version[0])


class C(object):
    def func(self):
        return 100
c = C()

c.func   # <bound method C.func of <__main__.C object at 0x7f610780b390>>
C.func   # python2: <unbound method C.func>     ### python3 <function C.func at 0x7f1b92d9b6a8>

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

t = B()
print(super(B, t))
print(super(A, t))