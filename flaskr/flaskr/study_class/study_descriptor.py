


class MyDescriptor(object):
    """
    A simple demo descriptor
    """
    def __init__(self, init_value=None, name='my_var'):
        self.var_name = name
        self.value = init_value

    def __get__(self, obj, objtype):
        print 'Getting', self.var_name
        print obj, objtype
        return self.value

    def __set__(self, obj, value):
        msg = 'Setting {name} to {value}'
        print(msg.format(name=self.var_name, value=value))
        self.value = value


class MyClass(object):
    desc = MyDescriptor(init_value='Mike', name='desc')
    normal = 10


def test():
    c = MyClass()
    print c.desc
    print c.normal
    c.desc = 100
    print c.desc

test()
        