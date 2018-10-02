import types


class C(object):
    pass

def func(self):
    print('haha')

c = C()
c.func = types.MethodType(func, c)

# c.func()

try:
    C.func()
except AttributeError:
    pass


class Function(object):

    def __get__(self, obj, objtype=None):
        """Simulate func_descr_get() in Objects/funcobject.c"""
        if obj is None:
            return self
        return types.MethodType(self, obj)


class D(object):

    def f(self, x):
        return x

d = D()


# Access through the class dictionary does not invoke __get__.
# It just returns the underlying function object.
D.__dict__['f']     # <function f at 0x7fca82d85d70>


# Dotted access from a class calls __get__() which just returns
# the underlying function unchanged.
D.f     # python3 <function D.f at 0x7f4efd0f9048>  # python2 <unbound method D.f>
# print(D.f.__qualname__)   # only for python3

# Dotted access from an instance calls __get__() which returns the
# function wrapped in a bound method object
d.f     # python3 <bound method D.f of <__main__.D object at 0x7ff28b796320>> # same of python2


# Internally, the bound method stores the underlying function,
# the bound instance, and the class of the bound instance.
d.f.__func__ # python3 <function D.f at 0x7f7b17ccc048>  # python2 <function f at 0x7f5bf2f0bd70>

d.f.__self__     # python3 <__main__.D object at 0x7ff5b8cfe320> # same of python2
d.f.__class__    # python3 <class 'method'>  # python2 <type 'instancemethod'>




# 1. Emultate staticmethod
class StaticMethod(object):
    """Emulate PyStaticMethod_Type() in Objects/funcobject.c"""
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f

class E(object):

    def f(x):
        return x

    def g(x):
        return x + 100

    f = staticmethod(f)
    g = StaticMethod(g)

e = E()
assert E.f(100) == 100
assert e.f(100) == 100

E.g     # <function E.g at 0x7fb999a1a1e0>
e.g     # <function E.g at 0x7ffba58e61e0>

assert E.g(100) == 200
assert e.g(100) == 200