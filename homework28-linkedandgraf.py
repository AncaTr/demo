class Edge:
    def __init__(self, next_node=None, value=None, directed=True):
        self.next = next_node
        self.value = value
        self.directed = directed

class Node:
    def __init__(self, name, edges=None, value=None):
        self.name = name
        self.edges = edges if edges else []

        # If the node has a value, store it
        self.value = value
def find_shortest_path(start_node, dest_node):
    shortest_path = {}  # Placeholder for the shortest path calculation
    pass  # Your implementation here
Oradea = Node("Oradea")
Alba = Node("Alba")
Turda = Node("Turda")
Oradea.edges = [Edge(Alba, 250), Edge(Turda, 60)]
Alba.edges = [Edge(Oradea, 250), Edge(Turda, 200)]
Turda.edges = [Edge(Oradea, 60), Edge(Alba, 200)]
find_shortest_path(Oradea, Alba)
solutia corecta
class Edge:
    def __init__(self, next_node=None, value=None, directed=True):
        self.next = next_node
        self.value = value
        self.directed = directed

class Node:
    def __init__(self, name, edges=None, value=None):
        self.name = name
        self.edges = edges if edges else []

        # If the node has a value, store it
        self.value = value

class Graph:
    def __init__(self, directed=True):
        self.nodes = {}
        self.directed = directed

    def add_node(self, name, value=None):
        if name not in self.nodes:
            self.nodes[name] = Node(name, value=value)

    def add_edge(self, source_node_name, dest_node_name, value=None):
        if source_node_name not in self.nodes:
            self.add_node(source_node_name)
        if dest_node_name not in self.nodes:
            self.add_node(dest_node_name)

        source_node = self.nodes[source_node_name]
        dest_node = self.nodes[dest_node_name]

        edge = Edge(dest_node, value, self.directed)
        source_node.edges.append(edge)

        if not self.directed:
            reverse_edge = Edge(source_node, value, self.directed)
            dest_node.edges.append(reverse_edge)

def find_shortest_path(start_node, dest_node):
    shortest_path = {}
    pass

# Example Usage:
# Create a directed graph with values
graph = Graph(directed=True)
graph.add_edge("Oradea", "Alba", 250)
graph.add_edge("Oradea", "Turda", 60)
graph.add_edge("Alba", "Oradea", 250)
graph.add_edge("Alba", "Turda", 200)
graph.add_edge("Turda", "Oradea", 60)
graph.add_edge("Turda", "Alba", 200)

# Create an undirected graph without values
undirected_graph = Graph(directed=False)
undirected_graph.add_edge("X", "Y")
undirected_graph.add_edge("Y", "Z")

# Function call
find_shortest_path(graph.nodes["Oradea"], graph.nodes["Alba"])
