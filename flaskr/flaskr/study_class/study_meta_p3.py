


# 1. A metaclass is a class whose instances are classes.

# 2. There are numerous use cases for metaclasses. Just to name a few:
#    (1). logging and profiling
#    (2). interface checking
#    (3). registering classes at creation time
#    (4). automatically adding new methods
#    (5). automatic property creation
#    (6). proxies
#    (7). automatic resource locking/synchronization.

class MyMeta(type):
    def __new__(cls, clsname, bases, attributedict):
        print('cls: ', cls)
        print('clsname: ', clsname)
        print('bases: ', bases)
        print('attributedict: ', attributedict)
        print(type(attributedict))
        return type.__new__(cls, clsname, bases, attributedict)

class S(object):
    pass

class A(S, metaclass=MyMeta):
    pass

print(A)
print(A.__dict__.__class__)
print(type(A))      # <class '__main__.MyMeta'>




# x = input("Do you need the answer? (y/n): ")
x = 'y'

if x.lower() == "y":
    required = True
else:
    required = False
    
def the_answer(self, *args):
    return 42

class AugmentAnswers(type):
    def __init__(cls, clsname, bases, attributedict):
        if required:
            cls.the_answer = the_answer

class Philosopher1(object, metaclass=AugmentAnswers):
    pass

class Philosopher2(object, metaclass=AugmentAnswers):
    pass

class Philosopher3(object, metaclass=AugmentAnswers):
    pass

plato = Philosopher1()
print(plato.the_answer())
kant = Philosopher2()
# let's see what Kant has to say :-)
print(kant.the_answer())





