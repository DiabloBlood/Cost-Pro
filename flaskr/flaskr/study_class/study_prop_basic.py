import sys
sys.path.append('/var/www/report/zcur/flaskr/flaskr/')
from util.util import show_descr, is_descr



class MyProperty(object):
    """Emulate PyProperty_Type() in Objects/descrobject.c"""
    
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class C(object):

    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = MyProperty(getx, setx, delx, "I'm the 'x' property.")

c = C()
assert c.x is None
c.x = 100
assert c.x == 100

assert is_descr(MyProperty)
assert is_descr(MyProperty())


def getter(self):
    print 'Get from {}'.format(self)

def setter(self, value):
    print 'Set {} to {}'.format(self, value)

def deleter(self):
    print 'Delete from {}'.format(self)

p = MyProperty()

p = p.getter(getter)

p = p.setter(setter)

p = p.deleter(deleter)

assert p.fget is getter
assert p.fset is setter
assert p.fdel is deleter


class D(object):
    x = p

d = D()

assert D.x.fget is getter
assert D.x.fset is setter
assert D.x.fdel is deleter

        




