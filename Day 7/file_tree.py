class Node:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.adjacency_set = set()

    def add_edge(self, n):
        self.adjacency_set.add(n)

    def get_adjacent_edges(self):
        return self.adjacency_set

    def get_adjacent_edge(self, edge_name):
        for edge in self.adjacency_set:
            if edge.get_name() == edge_name:
                return edge

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size


class FileTree:
    def __init__(self):
        self.node_list = []

    def add_node(self, n):
        self.node_list.append(n)

    def add_edge(self, n1, n2):
        for node in self.node_list:
            if node == n1:
                node.add_edge(n2)

    def get_parent(self, n):
        for i in range(len(self.node_list)):
            for dest in self.node_list[i].get_adjacent_edges():
                if dest == n:
                    return self.node_list[i]

    def get_adjacent_edges(self, v):
        return self.node_list[v].get_adjacent_edges()


def depth_first(file_tree, visited, current=0):
    if visited[current] == 1:
        return
    visited[current] = 1
    print("Visited ", current)

    for edge in file_tree.get_adjacent_vertices(current):
        depth_first(file_tree, visited, edge)
