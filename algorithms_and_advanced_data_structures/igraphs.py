"""
3. Install igraph for Python. This might be helpful: 
http://hal.elte.hu/~nepusz/development/igraph/tutorial/tutorial.html

4. Using the graph example (stored in the variable, graph) in guido.py write a function that 
uses igraph to output the highest degree node, the average degree, whether or not the graph 
is bipartite, and the diameter. Include comments that explains what each of these things mean.

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

"""
from igraph import Graph


def create_graph(vertice,edges=[]):
    """Create a graph using igraph
    :add_vertices() method of the Graph class adds the given number of vertices to the graph.
    :add_edges() method of the Graph class adds edges, they are specified by pairs of integers,
     so [(0,1), (1,2)] denotes a list of two edge. igraph uses integer vertex IDs starting from zero
    """
    graph = Graph(directed=True)
    graph.add_vertices(vertice)
    graph.add_edges(edges)
    return graph


def highest_degree_node(graph):
    """Return the node with the maximum degree.
    Degree: The degree of a node equals that number of edges adjacent to it.

    :degree() method of the Graph class that returns the degree for each node.
     The methods accept a node id or a list of nodes ids (and if they are omitted,
     the default is the set of all vertices).
     @param graph: Graph object

    """
    degs = graph.degree()
    m = max(degs)
    return [i for i,j in enumerate(degs) if j == m]


def average_degree(graph):
    """Return the average degree of the graph (using degree() method).
    - sum(l)/float(len(l))
    @param graph: Graph object
    @return_type: float, 2 decimals

    """
    degree = graph.degree()
    return sum(degree)/float(len(degree))


def is_bipartite(graph):
    """Return True if the Graph is bipartite: https://en.wikipedia.org/wiki/Bipartite_graph

    igraph provides the functionality of is_bipartite
    :is_bipartite() method of the Graph class that decides whether the graph is bipartite or not.
    @param graph: Graph object

    """
    return graph.is_bipartite()

def graph_diameter(graph):
    """Returns the diameter of the graph. The diameter is the lenght of the shortest path between
    the most distanced nodes.

    igraph provides the functionality of calculate the diameter
    :diameter() method of the Graph class that calculates the diameter of the graph.
     Considers the edge directions while calculating the diameter.
    @param graph: Graph object.

    """
    return graph.diameter()

if __name__ == '__main__':
    # Create the same graph example stored in graph in guido.py using igraph
    graph = create_graph(['A', 'B', 'C', 'D', 'E', 'F'], [('A', 'B'),('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'C'), ('E', 'F'), ('F', 'C')])
    print "Edges of graph: ", graph.get_edgelist()
    print "Graph degree: ", graph.degree()
    print "Graph highest degree: ", highest_degree_node(graph)
    print "Average degree: ", '{:.2f}'.format(average_degree(graph))
    print "Is graph bipartite: ", is_bipartite(graph)
    print "The diameter of the graph is: ", graph_diameter(graph)
