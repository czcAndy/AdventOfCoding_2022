class Node:
    def __init__(self, name, parent, size=0, is_directory=False):
        self._name = name
        self._size = size
        self._adjacency_set = set()
        self._is_directory = is_directory
        self._parent = parent

    def add_edge(self, n):
        self._adjacency_set.add(n)

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

    def get_parent(self):
        return self._parent


class FileTree:
    def __init__(self):
        self._node_list = []

    def add_node(self, n):
        self._node_list.append(n)

    def link_nodes(self, n1, n2):
        n1.add_edge(n2)
        if n2.get_size() > 0:
            self.update_size_all_nodes_to_root(n1, n2.get_size())

    def update_size_all_nodes_to_root(self, current_node, size):
        if current_node is None:
            return

        current_node.add_size(size)
        return self.update_size_all_nodes_to_root(current_node.get_parent(), size)

    def find_nodes_fulfill_point_a(self):
        return sum(
            node.get_size() for node in self._node_list if node.get_size() <= 100000 and node.is_directory() is True)

    def find_nodes_fulfill_point_b(self):
        total_size = 70000000
        update_size = 30000000
        occupied_size = self._node_list[0].get_size()
        available_size = total_size - occupied_size
        size_to_be_removed = update_size - available_size

        min_diff = total_size
        candidate_node_for_removal = self._node_list[0]
        for node in self._node_list:
            diff = node.get_size() - size_to_be_removed
            if min_diff > diff >= 0:
                min_diff = diff
                candidate_node_for_removal = node

        return candidate_node_for_removal.get_size()
