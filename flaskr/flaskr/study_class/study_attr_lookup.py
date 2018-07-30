


class Foo(object):

    x = 5

    def __getattribute__(self, attr_name):
        print attr_name
        print '__getattribute__ first invoke!'

foo = Foo()

print foo.x
