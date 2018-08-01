


class Foo(object):

    x = 5

    def __getattribute__(self, attr_name):
        print attr_name
        print '__getattribute__ first invoke!'

foo = Foo()


class A(object):
    def __getattribute__(self, attr_name):
        print '{} called'.format(self.__class__.__name__)

class B(A):
    pass

class C(B):
    x = 5
    def __getattribute__(self, attr_name):
        # print '{} called'.format(self.__class__.__name__)
        print 'haha'
        return super(object).__getattribute__(self, attr_name)

c = C()
c.x