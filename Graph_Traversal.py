class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        return [(e.value, e.node_from.value, e.node_to.value)
                for e in self.edges]

    def get_edge_list_names(self):
        return [(edge.value,
                self.node_names[edge.node_from.value],
                self.node_names[edge.node_to.value])
                for edge in self.edges]


    def get_adjacency_list(self):
        """Return a list of lists.
        The indecies of the outer list represent "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_index = self.find_max_index()
        adjacency_list = [[] for _ in range(max_index)]
        for edg in self.edges:
            from_value, to_value = edg.node_from.value, edg.node_to.value
            adjacency_list[from_value].append((to_value, edg.value))
        return [a or None for a in adjacency_list] # replace []'s with None

    def get_adjacency_list_names(self):
        """Each section in the list will store a list
        of tuples that looks like this:
        (To Node Name, Edge Value).
        Node names should come from the names set
        with set_node_names."""
        adjacency_list = self.get_adjacency_list()
        def convert_to_names(pair, graph=self):
            node_number, value = pair
            return (graph.node_names[node_number], value)
        def map_conversion(adjacency_list_for_node):
            if adjacency_list_for_node is None:
                return None
            return map(convert_to_names, adjacency_list_for_node)
        return [map_conversion(adjacency_list_for_node)
                for adjacency_list_for_node in adjacency_list]

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_index = self.find_max_index()
        adjacency_matrix = [[0] * (max_index) for _ in range(max_index)]
        for edg in self.edges:
            from_index, to_index = edg.node_from.value, edg.node_to.value
            adjacency_matrix[from_index][to_index] = edg.value
        return adjacency_matrix

    def find_max_index(self):
        """Return the highest found node number
        Or the length of the node names if set with set_node_names()."""
        if len(self.node_names) > 0:
            return len(self.node_names)
        max_index = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index

    def find_node(self, node_number):
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)
    
    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False


    def dfs_helper(self, start_node):
        ret_list = [start_node.value]
        start_node.visited = True
        for edge in start_node.edges:
            if not edge.node_to.visited:
                ret_list.extend(self.dfs_helper(edge.node_to))
        return ret_list

    def dfs(self, start_node_num):
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def dfs_names(self, start_node_num):
        return [self.node_names[num] for num in self.dfs(start_node_num)]

    def bfs(self, start_node_num):
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        ret_list = []
        queue = [start_node]
        start_node.visited = True

        while queue:
            node = queue.pop(0)
            ret_list.append(node.value)
            for edge in node.edges:
                if not edge.node_to.visited:
                    queue.append(edge.node_to)
                    edge.node_to.visited = True

        return ret_list

    def bfs_names(self, start_node_num):
        return [self.node_names[num] for num in self.bfs(start_node_num)]

graph = Graph()

graph.set_node_names(('Mountain View', 'San Francisco', 'London', 'Shanghai', 'Berlin', 'Sao Paolo', 'Bangalore'))

graph.insert_edge(51, 0, 1)
graph.insert_edge(51, 1, 0)
graph.insert_edge(9950, 0, 3)
graph.insert_edge(9950, 3, 0)
graph.insert_edge(10375, 0, 5)
graph.insert_edge(10375, 5, 0)
graph.insert_edge(9900, 1, 3)
graph.insert_edge(9900, 3, 1)
graph.insert_edge(9130, 1, 4)
graph.insert_edge(9130, 4, 1)
graph.insert_edge(9217, 2, 3)
graph.insert_edge(9217, 3, 2)
graph.insert_edge(932, 2, 4)
graph.insert_edge(932, 4, 2)
graph.insert_edge(9471, 2, 5)
graph.insert_edge(9471, 5, 2)

import pprint
pp = pprint.PrettyPrinter(indent=2)

print("Edge List")
pp.pprint(graph.get_edge_list_names())

print("\nAdjacency List")
pp.pprint(graph.get_adjacency_list_names())

print("\nAdjacency Matrix")
pp.pprint(graph.get_adjacency_matrix())

print("\nDepth First Search")
pp.pprint(graph.dfs_names(2))

print("\nBreadth First Search")
pp.pprint(graph.bfs_names(2))
