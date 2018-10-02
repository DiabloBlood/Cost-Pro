


class Philosopher1(object): 
    def the_answer(self, *args):
        return 42
    
class Philosopher2(object): 
    def the_answer(self, *args):
        return 42
    
class Philosopher3(object): 
    def the_answer(self, *args):
        return 42
    
plato = Philosopher1()
# print(plato.the_answer())
kant = Philosopher2()
# let's see what Kant has to say :-)
# print(kant.the_answer())



class Answers:
    def the_answer(self, *args):
        return 42
    
class Philosopher1(Answers): 
    pass
class Philosopher2(Answers): 
    pass
class Philosopher3(Answers): 
    pass

plato = Philosopher1()
print(plato.the_answer())
kant = Philosopher2()
# let's see what Kant has to say :-)
print(kant.the_answer())


# the following variable would be set as the result of a runtime calculation:
# x = raw_input("Do you need the answer? (y/n): ")      # if python 2
x = input("Do you need the answer? (y/n): ")

if x == 'y':
    required = True
else:
    required = False

def the_answer(self, *args):
    return 42
    
class Philosopher1(object): 
    pass
if required:
    Philosopher1.the_answer = the_answer
    
class Philosopher2(object): 
    pass
if required:
    Philosopher2.the_answer = the_answer
    
class Philosopher3(object): 
    pass
if required:
    Philosopher3.the_answer = the_answer

plato = Philosopher1()
kant = Philosopher2()
# let's see what Plato and Kant have to say :-)
'''
if required:
    print(kant.the_answer())
    print(plato.the_answer())
else:
    print("The silence of the philosphers")
'''


if x == 'y':
    required = True
else:
    required = False

def the_answer(self, *args):
    return 42

def augment_answer(cls):
    if required:
        cls.the_answer = the_answer
    return cls


@augment_answer
class Philosopher1(object):
    pass

@augment_answer
class Philosopher2(object):
    pass

@augment_answer
class Philosopher3(object):
    pass

    
plato = Philosopher1()
kant = Philosopher2()
# let's see what Plato and Kant have to say :-)
if required:
    print(kant.the_answer())
    print(plato.the_answer())
else:
    print("The silence of the philosphers ************")