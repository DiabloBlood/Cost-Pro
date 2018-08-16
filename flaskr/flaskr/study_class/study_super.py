


def print_init(obj):
    print('{} init'.format(obj.__class__.__name__))


class A(object):
    def __init__(self):
        print_init(self)


class B(A):
    def __init__(self):
        print_init(self)



# 1. super() only works for new-style classes
# 2. If the second argument is an object, isinstance(obj, type) must be true

try:
    super(B, 5)
except TypeError:
    pass

t = B()
print(super(B, t))
print(super(A, t))