# -*- coding: utf-8 -*-


# 1. Dashed Arrow Up Rule:If X is an instance of A, and A is a subclass of B, then X is an instance of B as well.
# 2. Dashed Arrow Down Rule:If B is an instance of M, and A is a subclass of B, then A is an instance of M as well.

# Exmamples
# 1. Dashed Arrow Up Rule
# print '5 is an instance of int: {}'.format(isinstance(5, int))
# print 'int is a subclass of object: {}'.format(int.__bases__[0] is object)
# print '5 is an instance of object: {}'.format(isinstance(5, object))

# print '***************************************************'

# 2. Dashed Arrow Down Rule
class MyInt(int):
    pass

# print 'int is an instance of type: {}'.format(int.__class__ is type)
# print 'MyInt is a subclass of int: {}'.format(MyInt.__bases__[0] is int)
# print 'MyInt is and instance of type: {}'.format(MyInt.__class__ is type)
# print '***************************************************'

# 推导: type是type的实例. 已知: object是type的基类, object是type的实例, 利用Dashed Arrow Down Rule (Rule 2)
print 'object is an instance of type: {}'.format(object.__class__ is type)
print 'type is a subclass of object: {}'.format(type.__bases__[0] is object)
print 'type is an instance of type: {}'.format(type.__class__ is type)
print '***************************************************'

#推导: object是object的实例. 已知: object是type的实例, object是type的基类(type是object的子类), 利用Rule 1
print 'object is an instance of type: {}'.format(object.__class__ is type)
print 'type is a subclass of object: {}'.format(type.__bases__[0] is object)
print 'object is an instance of object: {}'.format(isinstance(object, object))
print '***************************************************'

# 推导: object是type的实例.
print 'object is an instance of type: {}'.format(object.__class__ is type)
print '***************************************************'

#自举过程:
# 1. 先build基类object, 不继承自任何类, 所以 object.__bases__ = ()
# 2. build子类type(继承于object), 所以 type.__bases__ = (<type 'object'>,)
# 3. 赋值 object.__class__ = <type 'type'>, 将object定义为类型对象(type object)
# 4. 赋值 type.__class__ = <type 'type'>, 将type定义为类型对象(type object)

# [Basic Concepts] The Object Within
# 1. Identity
# 2. A value
# 3. A type
# 4. One or more Bases

# 新概念： [type objects]
# type和object都属于type objects. type objects翻译过来就是类型对象了. 类型对象都的特征：

# 1. 它们用于表示程序中的抽象数据类型. 例如，我们定义的一个类User会代表系统中所有的用户. int会代表系统中所有数字.
# 2. 它们能被继承. 这意味着你可以利用存在的类型对象创造出新的类型对象. 已经存在的类型对象是新的类型对象的超类.
# 3. 它们能被实例化. 这意味着你可以利用已经存在的类型对象创造出新的实例对象. 前者是后者的type.
# 4. 类型对象的类型是type. type和object的类型均为type
# 5. 它们有时会被成为类型有时会被称为类。

# 你没有看错. 在新版本的python中类和类型已经是同一样东西了.
# 由一个很明显的地方就可以看出来. __class__和type()的输出是一样的.

# 在旧版本的python中, 类是特指用class语句创造出来的东西. 而内置类型例如int一般不会被认为是类, 而是被认为是类型.
# 但在新版本中它们是同一样东西了. 我觉得有必要为这个改变定义一条规则：类是类型, 类型也是类（Class is Type is Class）

# 在python中只有两种对象: 类型和非类型. 非类型也被称为实例.
# 这里有英文原句，我不知怎么翻译了，很容易看懂，但不知如何说：
# There are only two kinds of objects in Python: to be unambiguous let's call these types and non-types.
# Non-types could be called instances, but that term could also refer to a type,
# since a type is always an instance of another type. Types could also be called classes,
# and I do call them classes from time to time.

'''
print object                # <type 'object'>      object是一个类实例, class instance
print type                  # <type 'type'>        type是类的类, 类的模板template
print object.__class__      # <type 'type'>        object是type的一个实例
print object.__bases__      # ()                    object没有任何父类
print type.__class__        # <type 'type'>        type是类type的一个实例
print type.__bases__        # (<type 'object'>,)    type的父类是object

# type is the type of all types, which definite all types. object is the base of all the other types, 所以object没有base
# 
print isinstance(object, object) # True
print isinstance(type, object)   # True
'''


# 这些内容是对前面的总结:

# 1: 在python中有两种对象:
# 类型对象: 可以被实例化和继承;
# 非类型对象: 不可以被实例和继承.

# 2. <class 'type'>和<class 'object'>是python中的两个源对象.
# 3. 每个对象都有类型. 用objectname.__class__查看.
# 4. 每个类型对象都有超类.(object除外)用objectname.__bases__可以查看.
# 5. 通过继承产生的新对象都是类型对象. 继承是用class语句来实现的. 
# 6. 通过实例化产生的新对象可能是类型对象，也可能是非类型对象. 实例化是通过调用操作符()来实现的.
# 7. 一些python的非类型对象可以通过特殊的语法来创造. 例如[1, 2, 3]是list的实例.
# 8. 在内部，python总是使用类型对象来创造新对象. 新创造的对象是该类型对象的实例.
#    (在这里，实例有两种意思: 一通过继承产生的子类, 二是通过实例化产生的具体实例. 但平时我们说的实例就是只第二).
# 9. python通过class语句中指定的超类的类型来决定新对象的类型。


# 10. issubclass(A, B)返回true当且仅当:
# B在A.__bases__输出的元组之中;
# 如果A在Z.__bases__输出的元组中，issubclass(Z,B)返回true.
# isinstance(A, B)返回true当且仅当：
# A.__class__是B，或者
# issubclass(A.class, B)返回true.