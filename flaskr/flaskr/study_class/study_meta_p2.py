


# 1. A metaclass is a class whose instances are classes.

# 2. There are numerous use cases for metaclasses. Just to name a few:
#    (1). logging and profiling
#    (2). interface checking
#    (3). registering classes at creation time
#    (4). automatically adding new methods
#    (5). automatic property creation
#    (6). proxies
#    (7). automatic resource locking/synchronization.

class MyMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print('cls: ', cls)
        print('clsname: ', clsname)
        print('superclasses: ', superclasses)
        print('attributedict: ', attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)

class S(object):
    pass

class A(S):
    __metaclass__ = MyMeta
    pass

# We can see MyMeta.__new__ has been called and not type.__new__.
a = A()

a                   # <__main__.A object at 0x7f9c016c9f10>
a.__class__         # <class '__main__.A'>
A.__metaclass__     # <class '__main__.MyMeta'>


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))