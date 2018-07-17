
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

s = Student('sichao', 99)
# print dir(s)
# instance s will has an extra variable __name
s.__name = 'haha'
# print s.get_name()
# print s.__name
# print dir(s)


class Animal(object):

    def run(self):
        print '{} is running...'.format(self.__class__.__name__)


class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
# dog.run()

cat = Cat()
# cat.run()



# Polymorphism, dog is Animal instance
# print isinstance(dog, Animal)

# print type(dog) == dog.__class__

# print isinstance([1, 2, 3], (list, tuple))


# When use hasattr?
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None


# How to use __slots__

class Student(object):
    pass

s = Student()
s.name = 'Michael'
# print s.name


def set_age(self, age):
    self.age = age

from types import MethodType

# Assgin instance method
s.set_age = MethodType(set_age, s)
s.set_age(25) 
# print s.age

s2 = Student()
# s2.set_age(25)


# Assign class method
# @classmethod
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
# print s.score

s2.set_score(99)
# print s2.score
# print s.score

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.score = 90