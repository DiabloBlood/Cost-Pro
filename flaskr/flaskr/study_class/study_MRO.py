


# 1. Given a class C in a complicated multiple inheritance hierarchy, it is a non-trivial task to specify
#    the order in which methods are overridden, i.e. to specify the order of the ancestors of C.

# 2. The list of the ancestors of a class C, including the class itself, ordered from the nearest ancestor
#    to the furthest, is called the class precedence list or the linearization of C.

# 3. The Method Resolution Order (MRO) is the set of rules that construct the linearization. In the Python
#    literature, the idiom "the MRO of C" is also used as a synonymous for the linearization of the class C.

# 4. For instance, in the case of single inheritance hierarchy, if C is a subclass of C1, and C1 is a subclass
#    of C2, then the linearization of C is simply the list [C, C1 , C2]. However, with multiple inheritance
#    hierarchies, the construction of the linearization is more cumbersome, since it is more difficult to
#    construct a linearization that respects local precedence ordering and monotonicity.

# 5. I will discuss the local precedence ordering later, but I can give the definition of monotonicity here.
#    A MRO is monotonic when the following is true: if C1 precedes C2 in the linearization of C, then C1
#    precedes C2 in the linearization of any subclass of C. Otherwise, the innocuous operation of deriving
#    a new class could change the resolution order of methods, potentially introducing very subtle bugs.
#    Examples where this happens will be shown later.

# 6. Not all classes admit a linearization. There are cases, in complicated hierarchies, where it is not
#    possible to derive a class such that its linearization respects all the desired properties.


def get_cur_name(name):
    if name == 'object':
        return 'O'
    return name

from collections import deque
def get_mro(objclass):
    result = []
    queue = deque([objclass])
    while queue:
        cur = queue.popleft()
        if cur.__bases__:
            queue.extend(cur.__bases__)
        # should use visitid map to implemented
        cur_name = get_cur_name(cur.__name__)
        if cur_name not in result:
            result.append(cur_name)
    ori_mro = [get_cur_name(item.__name__) for item in objclass.mro()]
    print objclass.__name__, ': ', result, cmp(result, ori_mro)

class X(object): pass
class Y(object): pass
class A(X, Y): pass
class B(Y, X): pass
'''TypeError: Error when calling the metaclass bases. Cannot create a consistent method resolution
   order (MRO) for bases X, Y
'''
# class C(A, B): pass
# get_mro(A)
# get_mro(B)


O = object
class F(O): pass
class E(O): pass
class D(O): pass
class C(D, F): pass
class B(D, E): pass
class A(B, C): pass

# get_mro(B)
# get_mro(C)
# get_mro(A)

class A(object): pass
class B(object): pass
class C(object): pass
class D(object): pass
class E(object): pass
class K1(A, B, C): pass
class K2(D, B, E): pass
class K3(D, A): pass
class Z(K1, K2, K3): pass

get_mro(A)
get_mro(B)
get_mro(C)
get_mro(D)
get_mro(K1)
get_mro(K2)
get_mro(K3)
get_mro(Z)

print [get_cur_name(item.__name__) for item in Z.mro()]



