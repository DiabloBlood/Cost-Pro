


class Foo(object):
    pass

print Foo.__bases__

Foo = type('Foo', (), {})

print Foo.__bases__

def always_false(self):  
    return False 

Foo = type('Foo', (), {'always_false': always_false})

print dir(Foo)