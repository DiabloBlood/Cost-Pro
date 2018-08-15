# -*- coding: utf-8 -*-


# If your class contain both getattr and getattribute magic methods then  __getattribute__ is called first.
# But if  __getattribute__ raises  AttributeError exception then the exception will be ignored and __getattr__
# method will be invoked. See the following example:

class C(object):

    def __init__(self):
        self._x = 100

    def __getattribute__(self, key):
        print '__getattribute__() of key[{}] is called'.format(key)
        return object.__getattribute__(self, key)

    def __getattr__(self, key):
        print '__getattr__() of key[{}] is called'.format(key)

    @property
    def x(self):
        return self._x


c = C()
print dir(c) # will call __dict__, __members__, __methods__