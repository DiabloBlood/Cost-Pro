

def foo():
    for i in range(3):
        print(id(i))

print range(5)
foo()