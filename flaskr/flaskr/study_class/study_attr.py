# -*- coding: utf-8 -*-


class C(object):

    a = 'abc'

    def __getattribute__(self, *args, **kwargs):
        print '__getattribute__() is called'
        return object.__getattribute__(self, *args, **kwargs)
        # return 'haha'

    def __getattr__(self, name):
        print '__getattr__() is called'
        return name, 'from getattr'

    def __get__(self, obj, objtype):
        print '__get__() is called', obj, objtype
        return self

    def foo(self, x):
        print x


class C2(object):
    d = C()


def test():
    c = C()
    c2 = C2()
    print '__delattr__' in object.__dict__.keys()
    print C2.__dict__.keys()
    print c.__dict__
    # print C.a
    # print C.d
    # print c.a
    # print c.zzzz
    # print c2.d
    # print c2.d.a

test()

# 小结: 
# 1. 可以看出, 每次通过实例访问属性, 都会经过__getattribute__函数. 
# 2. 而当属性不存在时, 仍然需要访问__getattribute__, 不过接着要访问__getattr__. 这就好像是一个异常处理函数. 
# 3. 每次访问descriptor(即实现了__get__的类), 都会先经过__get__函数.