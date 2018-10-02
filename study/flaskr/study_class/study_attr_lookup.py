def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]


class A(object):

    x = 5

    __slots__ = ('a', 'b')

    def __init__(self):
        self.a = 1
        self.b = 2

class B(object):
    pass

t = A()
t2 = B()
print t.x
print type(t.__slots__)
print dir(A)