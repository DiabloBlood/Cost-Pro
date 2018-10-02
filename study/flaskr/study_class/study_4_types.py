# -*- coding: utf-8 -*-


x = 10

expr = """
z = 30
sum = x + y + z
print(sum)
"""

d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

def foo():
    y = 20
    exec(expr)
    exec(expr, d1)
    exec(expr, d1, d2)
    
foo()

# print d1.keys()
# print d2.keys()


# type和class绝对不同。 

# Python里面的所有对象，都是由type制造的。相应的type制造一个blanket的对象
# 然后解释器再根据你的源代码，往这个blank的对象里面塞东西。 

# 空白的class object是由types.ClassType或者types.TypeType创建的。而你写的代码
# 会先在一个dict里面运行，然后塞进这个blank的class object里面。 

code = """
def func(self): 
    print "blah, blah, blah"
"""

d = {}
exec(code, d)

import types

print types.ClassType.__class__

old_class = types.ClassType('OldClass', (), d)
o = old_class()
o.func()

new_class = types.TypeType('NewClass', (), d)
o = new_class()
o.func()


print '********************************'

print types.ClassType
print type(types.ClassType)

print types.TypeType
print type(types.TypeType)

print type(types.TypeType).__class__

print types.MethodType
print type(types.MethodType)