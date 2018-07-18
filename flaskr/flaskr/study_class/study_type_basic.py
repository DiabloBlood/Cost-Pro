# -*- coding: utf-8 -*-

'''
class Foo(object):
    pass

print Foo.__bases__
print Foo

Foo = type('Foo', (), {})

print Foo

print Foo.__bases__

def always_false(self):  
    return False 

Foo = type('Foo', (), {'always_false': always_false})

print type(Foo)
print Foo

print '********************'

foo = Foo()

print foo
print type(foo)
print foo.__class__
print foo.__class__.__class__
'''

class Foo(type):
    pass

print Foo
print type(Foo)
print Foo.__bases__


class Foo(object):
    pass

print Foo
print type(Foo)
print Foo.__bases__

class Foo:
    pass

print Foo
print type(Foo)
print Foo.__bases__

class Foo(int):
    pass

print Foo
print type(Foo)
print Foo.__bases__

# 遗留问题, 新式类, 经典类, 多继承
# 新式类广度优先搜索继承类的方法
# 经典类深度优先搜索继承类的方法

'''
python2 里的新式类, 其特点如下(截取Guido的博客内容, 然后添加点自己的解释, 轻拍~):
1. low-level constructors named __new__() – 低级别的构造函数.
2. Note: Python 的 class __init__ 并不是其他语言意义上的构造函数,在 new 创建实例后对实例属性初始化的函数.

3. descriptors, a generalized way to customize attribute access – 描述符.
或者说描述符协议支持.descriptor protocol __get__, __set__ ,__delete__ 等,可以阅读 descriptor 文档

4. static methods and class methods － 静态方法和类方法

5. properties (computed attributes) – 属性访问 setter getter.

6. decorators (introduced in Python 2.4) – 装饰器.现在装饰器语法糖遍布各Python框架.

7. slots – 用户设置后可以限定实例的属性.
    在 Python2 中替代 __dict__, 可以节省近 2/3 内存, Python3 中可以不因为优化内存使用率而使用 slots,
    因为 __dict__ 结构内存做了优化,
    Note: __dict__ 并不是 Python 意义上的内置的 dict, 其实是一个 proxy 类.

8. a new Method Resolution Order (MRO) – MRO 方法解析次序改变(由左递归改为C3算法)
'''