class Node:
    def __init__(self, name, size=0, is_directory=False):
        self._name = name
        self._size = size
        self._adjacency_set = set()
        self._is_directory = is_directory

    def add_edge(self, n):
        self._adjacency_set.add(n)
        self.add_size(n.get_size())

    def get_adjacent_nodes(self):
        return self._adjacency_set

    def get_adjacent_node(self, edge_name):
        for edge in self._adjacency_set:
            if edge.get_name() == edge_name:
                return edge

    def get_name(self):
        return self._name

    def get_size(self):
        return self._size

    def add_size(self, size):
        self._size += size

    def is_directory(self):
        return self._is_directory


class FileTree:
    def __init__(self):
        self._node_list = []

    def add_node(self, n):
        self._node_list.append(n)

    def add_edge(self, n1, n2):
        for node in self._node_list:
            if node == n1:
                node.add_edge(n2)

    def get_parent(self, n):
        for i in range(len(self._node_list)):
            for dest in self._node_list[i].get_adjacent_nodes():
                if dest == n:
                    return self._node_list[i]

    def get_adjacent_edges(self, v):
        return self._node_list[v].get_adjacent_nodes()

    def find_nodes_fulfill_point_a(self):
        return sum(
            node.get_size() for node in self._node_list if node.get_size() <= 100000 and node.is_directory() is True)
