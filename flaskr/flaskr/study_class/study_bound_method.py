


class C(object):

    def method_one(self):
        print "Called method_one"

    def method_two():
        print "Called method_two"

    @staticmethod
    def method_three():
        print "Called method_three"


c = C()
# c.method_one()

# TypeError: method_two() takes no arguments (1 given)
# c.method_two()

def test_1():
    # <bound method C.method_one of <__main__.C object at 0x7f7b651be390>>
    print c.method_one
    # <unbound method C.method_one>
    print C.method_one

    # <function method_three at 0x7f6dedc50d70>
    # The decorator tells the built-in default metaclass type (the class of a class)
    # to not create bound methods for method_three.
    print c.method_three
    print C.method_three


def test_2():
    # interpreter translate
    c.method_one()
    C.method_one(c)
    c.__class__.method_one(c)


def test_3():
    # print C.__dict__['method_one']      # <function method_one at 0x7ff61c6b5c80>
    # print C.__dict__['method_two']      # <function method_two at 0x7ff61c6b5cf8>
    # print C.__dict__['method_three']    # <staticmethod object at 0x7ff61c6b3da8>

    # As you can see if you access the method_one attribute on the class you get back an unbound method,
    # however inside the class storage (the dict) there is a function. Why's that?
    # The reason for this is that the class of your class implements a __getattribute__ that resolves descriptors.
    # Sounds complex, but is not. C.method_one is roughly equivalent to this code in that special case:
    print C.__dict__['method_one'].__get__(None, C)     # <unbound method C.method_one>

    # That's because functions have a __get__ method which makes them descriptors.
    # If you have an instance of a class it's nearly the same, just that None is the class instance:

    #<bound method C.method_one of <__main__.C object at 0x7f06babb4450>>
    print C.__dict__['method_one'].__get__(c, C)

    # Now why does Python do that? Because the method object binds the first parameter of a function
    # to the instance of the class. That's where self comes from. Now sometimes you don't want your
    # class to make a function a method, that's where staticmethod comes into play:
    # The staticmethod decorator wraps your class and implements a dummy __get__ that returns
    # the wrapped function as function and not as a method:
    print C.__dict__['method_three'].__get__(None, C)   # <function method_three at 0x7fd1552d4d70>
    print C.__dict__['method_three'].__get__(c, C)      # <function method_three at 0x7fd1552d4d70>

# test_1()
# test_2()
test_3()