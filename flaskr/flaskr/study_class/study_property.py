

# 1. fget is a function for getting an attribute value.
#    fset is a function for setting an attribute value.
#    fdel is a function for deleting an attribute value.
#    And doc creates a docstring for the attribute.
class C(object):

    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

c = C()
assert c.x == None
c.x = 5
assert c.x == 5
assert c._x == 5

del c.x
try:
    c.x
except AttributeError:
    pass


class A(object):
    def __init__(self):
        self._v = 100

    @property
    def v(self):
        """Get the current voltage."""
        return self._v

a = A()
assert a.v == 100

assert A.v.fget(a) == 100
assert A.v.fset is None


class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

c = C()
assert c.x is None and c._x is None
c.x = 100
assert c.x == 100 and c._x == 100

assert C.x.fget(c) == 100
C.x.fset(c, 200)
assert c.x == 200 and c._x == 200


### p is <property object at 0x7f390f369aa0>
### property is <type 'property'>
p = property()
# <property object at 0x7f390f369aa0>
# <built-in method setter of property object at 0x7f390f369aa0>
# <built-in method getter of property object at 0x7f390f369aa0>
# <built-in method deleter of property object at 0x7f390f369aa0>

assert id(p.getter(None)) == id(p.setter(None)) == id(p.deleter(None)) != id(p)


def getter(self):
    print 'Get from {}'.format(self)

def setter(self, value):
    print 'Set {} to {}'.format(self, value)

def deleter(self):
    print 'Delete from {}'.format(self)

p = property()

p = p.getter(getter)

p = p.setter(setter)

p = p.deleter(deleter)

assert p.fget is getter
assert p.fset is setter
assert p.fdel is deleter

class Foo(object):
    pass

foo = Foo()
# p.__get__(foo, Foo)
# p.__set__(foo, 100)
# p.__delete__(foo)

class Bar(object):
    x = p

# bar = Bar()
# bar.x
# bar.x = 200
# del bar.x