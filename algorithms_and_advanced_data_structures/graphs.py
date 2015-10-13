"""
1. Write a class called Graph, Node, and Edge. The Graph should be able to contain Node and Edge 
    objects that implements the same interface as guido's list and dict implementation:
    a) `for node in graph`
    b) `for node in graph[node_name]`
    c) `graph.has_key(node_name)`

   The benefit of this implementation is now Nodes and Edges can contain metadata we have 
   immediate access to while not losing any of the functionality we've already got laying 
   around in the find_all_paths and find_shortest_paths methods.

   Ensure the node object we're getting out of the iterators in 4.1 a) and 4.1 b) are instances 
   of the Node class.

2. Write tests that uses the same `find_all_paths` and `find_shortest_path` method to show the two 
graph representations are interchangeable. 

"""
from guido import find_all_paths, find_shortest_path


class Graph(object):
    def __init__(self):
        """Initialize a graph.
        """
        self.edges = {}
        self.nodes = []

    def addNode(self, node):
        # Check that node is a Node object
        if not isinstance(node, Node):
            raise TypeError('%s is not of type Node' % node)
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge):
        # Check that edge is a Edge object
        if not isinstance(edge, Edge):
            raise TypeError('%s is not of type Edge' % edge)
        start = edge.start
        end = edge.end

        if not(start in self.nodes and end in self.nodes):
            raise ValueError('%s and %s must be in the graph' % (start, end))
        if (end in self.edges[start]):
            raise ValueError('The edge (%s, %s) is already in the graph' % (start, end))
        self.edges[start].append(end)

    def has_key(self,node):
        """Check if a given Node is part of the graph
        """
        if not isinstance(node, Node):
            raise TypeError('%s is not of type Node' % node)
        return node in self.nodes

    # for node in graph
    def __iter__(self):
        return self.nodes

    # graph[node]
    def __getitem__(self,node):
        """Return the neighbors of the given node.
        """
        if not isinstance(node, Node):
            raise ArgumentError('Graphs can only contain Nodes')
        return self.edges[node]

    # pretty printing
    def __repr__(self):
        return 'Graph(%d nodes, %d edges)' % (len(self.nodes), sum([len(value) for value in self.edges.values()]))


class Node(object):
    def __init__(self, name):
        self.name = str(name)

    def __hash__(self):
        """Key objects must be hashable.
        Needed to use Nodes as dictionary keys. Using the name makes it equivalent to strings
        """
        return hash(self.name)

    def __eq__(self, other):
        """Return whether this node is equal to another object.
        """
        # Nodes can be compared to other nodes only
        if isinstance(other, str):
            other = Node(other)
        if not isinstance(other, Node):
            return False
        return other.name == self.name

    # for pretty printing
    def __repr__(self):
        return 'Node: %s' % self.name


class Edge(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # for pretty printing
    def __repr__(self):
        return 'Edge:%s -> %s' % (self.start, self.end)

    # needed to use Edges as dictionary keys
    # (we use the text representation for simplicity)
    __hash__ = __repr__


def test_graph():
    """Test function with graph:
    g = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
    """
    nodes = []
    g = Graph()
    for node in map(chr, xrange(65, 71)):
        g.addNode(Node(node))

    g.addEdge(Edge(g.nodes[0],g.nodes[1]))
    g.addEdge(Edge(g.nodes[0],g.nodes[2]))
    g.addEdge(Edge(g.nodes[1],g.nodes[2]))
    g.addEdge(Edge(g.nodes[1],g.nodes[3]))
    g.addEdge(Edge(g.nodes[2],g.nodes[3]))
    g.addEdge(Edge(g.nodes[3],g.nodes[2]))
    g.addEdge(Edge(g.nodes[4],g.nodes[5]))
    g.addEdge(Edge(g.nodes[5],g.nodes[2]))

    return g

if __name__ == '__main__':
    g = test_graph()
    n1 = Node('A')
    n2 = Node('D')
    n3 = Node('C')
    print find_all_paths(g, n1, n2)
    print find_shortest_path(g, n1, n3)
