# -*- coding: utf-8 -*-


# (I) [study_1_class] some essentials of python class
# 1. __name变量被 interpreter 换名, 对instance重新赋值__name变量, 导致instance 产生新的__name变量.
# 2. isinstance([1, 2, 3], (list, tuple)) is True
# 3. type(dog) == dog.__class__

# 4. types, MethodType, runtime binding.
# 5. general runtime binding.

# 6. what is __slots__



# (II) [study_2_type] type vs. object
# 1. type and object relationship
#     ......
#     .    .>>
#   ..............____________>.............      
#   |    type    |<------------|   object  |
#   ..............             .............
#
#   (1). type is the subclass of object
#   (2). object is an instance of type
#   (3). type is an instance of type
#   Deduction
#   (4). object doesn't have any superclasses
#   (5). type's superclass is object
#   Essential deductions
#   (1). type object has attribute __bases__
#   (2). instance object doesn't has attribute __bases__
#   (3). All the type objects are instance of type. (Include type itself)
#   (4). User defined class is an instance of type.
#   Questions: object, type, object.__class__, object.__bases__, type.__class__, type.__bases__

# 2. basic type (int, list, tuple, dict, builtin_function_or_method, ...)
#   (1) int is a subclass of object
#   (2) int's type is type, which means int is a type object (built-in type object)

# 3. user defined type (keyword class defined classes)
#   (1). User defined class is an instance of type. (Inherited from type automatically by interpreter).
#   (2). User defined class's superclass depends on parentheses. (class Animal(object):pass class Dog(Animal):pass)



# (III) [study_3_type_basic] type make class
# 1. Foo = type('Foo', (), {})
#   (1). First arg: class name
#   (2). Second arg: super classes
#   (3). Third arg: name space
# 2. class Foo(object): pass => Foo = type('Foo', (), {})
# 3. 新式类 vs 经典类 (deep inside in the future)



# (IV) [study_4_types] exec built-in method, types module
# 1. exec(object[, globals[, locals]])
#   (1). First arg: code_str
#   (2). Second arg: globals variables dict
#   (3). Third arg: local variables dict
# 2. types module