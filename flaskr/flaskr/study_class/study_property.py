

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


class A(object):
    def __init__(self):
        self._v = 100

    @property
    def v(self):
        """Get the current voltage."""
        return self._v

a = A()
assert a.v == 100
a.v = 200
assert a.v == 200
