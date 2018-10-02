from collections import deque


class MRO(object):

    def __call__(self, objclass, is_print, is_dfs):
        return self.__get_mro(objclass, is_print, is_dfs)


    def __get_cur_name(self, name):
        if name == 'object':
            return 'O'
        return name


    def __add_indegree(self, indegree_map, node):

        if not node in indegree_map:
            indegree_map[node] = 0
        indegree_map[node] += 1


    def __dfs_build_graph_helper(self, node, graph, indegree_map):

        if not node in graph:
            graph[node] = []

        bases = node.__bases__
        for next_node in bases:
            graph[node].append(next_node)
            # ensure root indegree will not +1
            self.__add_indegree(indegree_map, next_node)
            self.__dfs_build_graph_helper(next_node, graph, indegree_map)

        if len(bases) > 1:
            for i in range(len(bases) - 1):
                this_node = bases[i]
                next_node = bases[i + 1]
                if not this_node in graph:
                    graph[this_node] = []
                graph[this_node].append(next_node)
                self.__add_indegree(indegree_map, next_node)


    def __dfs_build_graph(self, root_node):

        graph = {}
        indegree_map = {root_node: 0}
        self.__dfs_build_graph_helper(root_node, graph, indegree_map)

        return graph, indegree_map


    '''Should use dfs'''
    def __bfs_build_graph(self, root_node):

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
                self.__add_indegree(indegree_map, node)

            if len(bases) > 1:
                for i in range(len(bases) - 1):
                    node = bases[i]
                    if not node in graph:
                        graph[node] = []
                    graph[node].append(bases[i + 1])
                    self.__add_indegree(indegree_map, bases[i + 1])

            queue.extend(bases)

        return graph, indegree_map


    def __dfs_topo_sort(self, node, graph, indegree_map, result):
        for next_node in graph[node]:
            indegree_map[next_node] -= 1
            if indegree_map[next_node] == 0:
                result.append(next_node)
                self.__dfs_topo_sort(next_node, graph, indegree_map, result)


    def __bfs_topo_sort(self, root, graph, indegree_map, result):
        queue = deque([root])
        while queue:
            cur_node = queue.popleft()
            for node in graph[cur_node]:
                indegree_map[node] -= 1
                if indegree_map[node] == 0:
                    queue.append(node)

            result.append(cur_node)


    def __get_mro(self, objclass, is_print, is_dfs):

        # 1. build DAG
        if is_dfs:
            graph, indegree_map = self.__dfs_build_graph(objclass)
        else:
            graph, indegree_map = self.__bfs_build_graph(objclass)

        # 2. topological sort
        # the deeper class with indegree is 0 precedes shallow one
        root = [node for node in indegree_map if indegree_map[node] == 0][0]
        result = [root]

        if is_dfs:
            self.__dfs_topo_sort(root, graph, indegree_map, result)
        else:
            result = []
            self.__bfs_topo_sort(root, graph, indegree_map, result)

        if len(result) < len(indegree_map):
            raise ValueError('Cycle detected!')

        if is_print:
            ori_mro = [self.__get_cur_name(item.__name__) for item in objclass.mro()]
            formatted_res = [self.__get_cur_name(item.__name__) for item in result]
            print objclass.__name__, ': ', formatted_res, cmp(formatted_res, ori_mro)

        return result