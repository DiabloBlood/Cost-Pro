# -*- coding: utf-8 -*-


class C(object):
    x = 4

    def __init__(self, value=0):
        self.value = value


def test():
    c = C()
    # value会出现在实例对象的__dict__中
    print c.__dict__
    c.y = 5
    print c.__dict__
    print C.__dict__.keys()
    print C.__dict__['x']
    print c.__dict__.__class__


def test_1():

    # C.x = 5
    # print C.x
    # C.f = 5
    # print C.f

    c = C()
    c.y = 5
    # c.__dict__ = {}

    print dir(C.__dict__)
    # print C.__dict__.__class__
    # TypeError: 'dictproxy' object does not support item assignment
    # C.__dict__['x'] = 6
    # AttributeError: attribute '__dict__' of 'type' objects is not writable
    # C.__dict__ = {}

test()
# test_1()

# Notes:
# 1. The __dict__ of a type is a dictproxy object that is read only.
# 2. dictproxy class attribute 'keys' is a descriptor



class Object(object):
    pass


def test_2():
    obj = object()

    # AttributeError: 'object' object has no attribute '__dict__'
    # print obj.__dict__

    # AttributeError: 'object' object has no attribute 'name'
    # obj.name = 'haha'

    obj = Object()
    obj.name = 'haha'
    print obj.name

    print obj.__dict__

    # vars(obj)返回obj.__dict__
    print vars(obj)
    import inspect
    print inspect.getmembers(obj)


class Object_1(object):
    __slots__ = {}
    pass


def test_3():
    obj = Object_1()

    # 拥有 __slots__ 属性的类在实例化对象时不会自动分配 __dict__, 
    # 而obj.attr 即 obj.__dict__['attr'], 所以会引起 AttributeError
    # print obj.__dict__

    print obj.__slots__
    # AttributeError: 'Object' object has no attribute 'name'
    # obj.name = 'haha'
    # print obj.name

# test_2()
# test_3()

# 如何打印一个对象的所有属性和值的对?
# 1. 这个做法其实就是 theObject.__dict__, 也就是 vars(obj) 其实就是返回了o.__dict__
'''
for property, value in vars(theObject).iteritems():
    print property, ": ", value
'''

# 2. 两者不同的是, inspect.getmembers 返回的是元组 (attrname, value) 的列表.
# 而且是所有的属性, 包括 __class__, __doc__, __dict__, __init__ 等特殊命名的属性和方法.
# 而 vars() 只返回 __dict__. 对于一个空的对象来说. __dict__ 会是 {}, 而 inspect.getmembers 返回的不是空的。
'''
import inspect
for attr, value in inspect.getmembers(obj):
     print attr, value
'''