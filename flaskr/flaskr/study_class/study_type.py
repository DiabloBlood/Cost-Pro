# -*- coding: utf-8 -*-


# 1. Dashed Arrow Up Rule:If X is an instance of A, and A is a subclass of B, then X is an instance of B as well.
# 2. Dashed Arrow Down Rule:If B is an instance of M, and A is a subclass of B, then A is an instance of M as well.

# [Basic Concepts] The Object Within
# 1. Identity
# 2. A value
# 3. A type
# 4. One or more Bases

two = 2
# print type(two)         # <type 'int'>

# print type(int)         # <type 'type'>

# print int.__bases__       # (<type 'object'>,)
# print int.__class__

print object                # <type 'object'>      object是一个类实例, class instance
print type                  # <type 'type'>        type是类type的一个实例
print object.__class__      # <type 'type'>        object是type的一个实例
print object.__bases__      # ()                    object没有任何父类
print type.__class__        # <type 'type'>        type是类type的一个实例
print type.__bases__        # (<type 'object'>,)    type的父类是object

# type is the type of all types, whith definite all types. object is the base of all the other types, 所以object没有base
# 
print isinstance(object, object) # True
print isinstance(type, object)   # True