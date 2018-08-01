


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

def get_ori_mro(objclass):
    return [get_cur_name(item.__name__) for item in objclass.mro()]

def print_ori_mro(objclass):
    print objclass.__name__, ': ', get_ori_mro(objclass)

def get_cur_name(name):
    if name == 'object':
        return 'O'
    return name

from collections import deque
def get_mro_old(objclass):
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
    ori_mro = get_ori_mro(objclass)
    print objclass.__name__, ': ', result, cmp(result, ori_mro)


def get_mro(objclass):

    def add_indegree(indegree_map, node):
        if not node in indegree_map:
            indegree_map[node] = 0
        indegree_map[node] += 1


    def build_graph_dfs(root_node):

        def dfs_helper(node, graph, indegree_map):
            if not node in graph:
                graph[node] = []

            bases = node.__bases__
            for next_node in bases:
                graph[node].append(next_node)
                # ensure root indegree will not +1
                add_indegree(indegree_map, next_node)
                dfs_helper(next_node, graph, indegree_map)

            if len(bases) > 1:
                for i in range(len(bases) - 1):
                    this_node = bases[i]
                    next_node = bases[i + 1]
                    if not this_node in graph:
                        graph[this_node] = []
                    graph[this_node].append(next_node)
                    add_indegree(indegree_map, next_node)

        graph = {}
        indegree_map = {root_node: 0}
        dfs_helper(root_node, graph, indegree_map)

        return graph, indegree_map


    def build_graph_bfs(root_node):
        graph = {}
        indegree_map = {root_node: 0}
        queue = deque([root_node])

        while queue:
            cur_node = queue.popleft()
            bases = cur_node.__bases__

            if not cur_node in graph:
                graph[cur_node] = []

            for node in bases:
                graph[cur_node].append(node)
                add_indegree(indegree_map, node)

            if len(bases) > 1:
                for i in range(len(bases) - 1):
                    node = bases[i]
                    if not node in graph:
                        graph[node] = []
                    graph[node].append(bases[i + 1])
                    add_indegree(indegree_map, bases[i + 1])

            queue.extend(bases)

        return graph, indegree_map

    # 1. build DAG
    graph, indegree_map = build_graph_dfs(objclass)
    # 2. topological sort
    root = [node for node in indegree_map if indegree_map[node] == 0][0]
    result = [get_cur_name(root.__name__)]
    # the deeper class with indegree is 0 precedes shallow one
    def dfs_topo_sort(node, graph, indegree_map, result):
        for next_node in graph[node]:
            indegree_map[next_node] -= 1
            if indegree_map[next_node] == 0:
                result.append(get_cur_name(next_node.__name__))
                dfs_topo_sort(next_node, graph, indegree_map, result)

    root = [node for node in indegree_map if indegree_map[node] == 0][0]
    dfs_topo_sort(root, graph, indegree_map, result)
    # this is the BFS topological method
    '''
    queue = deque([node for node in indegree_map if indegree_map[node] == 0])
    while queue:
        cur_node = queue.popleft()
        for node in graph[cur_node]:
            indegree_map[node] -= 1
            if indegree_map[node] == 0:
                queue.append(node)

        result.append(get_cur_name(cur_node.__name__))
    '''

    if len(result) < len(indegree_map):
        raise ValueError('Cycle detected!')

    ori_mro = get_ori_mro(objclass)
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

get_mro(B)
get_mro(C)
get_mro(A)


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
# the most difficult case 1
get_mro(Z)


# what is good head?
# take the head of the first list, i.e L[B1][0]; if this head is not in the tail of any of the other lists,
# then add it to the linearization of C and remove it from the lists in the merge, otherwise look at the head
# of the next list and take it, if it is a good head. Then repeat the operation until all the class are removed
# or it is impossible to find good heads. In this case, it is impossible to construct the merge, Python 2.3
# will refuse to create the class C and will raise an exception.

class A1(object): pass
class A2(object): pass
class A3(object): pass
class B(A1, A2): pass
class C(A3): pass
class D(B, C): pass

# the most difficult case 2
get_mro(D)


