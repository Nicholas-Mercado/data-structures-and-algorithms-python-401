class Graph:
    """
    Put docstring here
    """

    def __init__(self):
       self._adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def size(self):
        return len(self._adjacency_list)

    def get_nodes(self):
        return self._adjacency_list.keys()


class Vertex:
    def __init__(self, value):
        self.value = value
