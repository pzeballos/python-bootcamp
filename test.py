import unittest
from random import randint
from algorithms_and_advanced_data_structures.guido import find_all_paths, find_shortest_path, graph
from loops_and_conditional_statements.loops import loop_range, loop_range_even, loop_random_values
from basic_data_structure_manipulation.data_structure import sort_random_values, filter_random_values,\
                                                              range_even, dictionary, gen_loop_range,\
                                                              gen_range_even, gen_random_values,\
                                                              gen_sort_random_values, gen_filter_random_values
from object_oriented_concepts.oo import Mammal, Cat, Dog, Dog2, Dog3
from algorithms_and_advanced_data_structures.graphs import Graph, Node, Edge, test_graph
from algorithms_and_advanced_data_structures.igraphs import create_graph, highest_degree_node,\
                                                            average_degree, is_bipartite, graph_diameter


class LoopsTestCase(unittest.TestCase):

    def test_range_values_iter(self):
        self.assertEqual(loop_range(1, 3), [1, 2])
        self.assertNotEqual(loop_range(2, 3), [1, 2, 3])
        # This task is for the particular case of values between 1 and 50:
        self.assertTrue(all(i != 0 and i <= 50 for i in loop_range()))

    def test_range_even_values(self):
        self.assertEqual(loop_range_even(0, 5), [0, 2, 4])
        self.assertNotEqual(loop_range(1, 6), [1, 3, 5])
        # This task is for the particular case of values between 0 and 50:
        self.assertTrue(all(i <= 50 for i in loop_range()))

    def test_generated_random_mumbers(self):
        self.assertNotIn(42, loop_random_values())
        # This task is for the particular case of values between 1 and 100:
        self.assertTrue(all(i != 0 and i <= 100 for i in loop_random_values()))


class DataStructureTestCase(unittest.TestCase):

    def test_sort_random_values(self):
        values = sort_random_values()
        sorted_values = sorted(values)
        self.assertEqual(sorted_values, values)

    def test_filter_random_values_to_match_range_values_iter(self):
        matched_values = filter_random_values()
        # Advantage of using `for`: we know the exact case which failed
        for i in matched_values:
            # in this case, the range of 1.1 is [1,50] and 1.3 does not contain 42
            self.assertLessEqual(i, 50)
            self.assertNotEqual(i, 42)
            self.assertNotEqual(i, 0)

    def test_range_even_values_lambda_version(self):
        # Advantage of using `all`: assert runs once so we have a fixed amount of asserts for test
        # without depending on the number of items of the list
        self.assertTrue(all(i % 2 == 0 for i in range_even()))

    def test_lambda_dictionary(self):
        d = dictionary()
        self.assertTrue(all(k+1 == v for k, v in d.iteritems()))

    def test_generators_object(self):
        self.assertTrue(all(i != 0 and i <= 50 for i in gen_loop_range))

        data2 = list(gen_range_even)    # make the generated list permanent
        self.assertTrue(all(i % 2 == 0 for i in data2))

        data3 = list(gen_random_values())
        self.assertNotIn(42, data3)
        # This particular task is for range [1,100], so I can add the tests:
        self.assertNotIn(0, data3)
        self.assertTrue(all(i <= 100 for i in data3))

        data4 = list(gen_sort_random_values())
        values = sorted(data4)  # make a copy
        self.assertEqual(data4, values)

        data5 = list(gen_filter_random_values())
        self.assertTrue(all(i <= 50 for i in data5))
        self.assertNotIn(0, data5)
        self.assertNotIn(42, data5)


class ObjectOrientedConceptsTestCase(unittest.TestCase):
    def test_mammal_class(self):
        """Test case:
        * Mammal should have a method called 'speak' that returns 'hello'.
        * Mammal should have a method called 'legs' that returns 2.
        * The output of 'legs' can be overwritten by modifying the _legs attribute of the Mammal class.
        """
        mammal = Mammal()
        self.assertEqual(mammal.speak(), 'hello')
        self.assertEqual(mammal.legs(), 2)
        mammal._legs = 4
        self.assertEqual(mammal.legs(), 4)

    def test_cat_class(self):
        """Test case:
        * Cat's speak method should return 'meow'.
        * Cat's 'legs' method should return 2.
        """
        cat = Cat()
        self.assertEqual(cat.speak(), 'meow')
        self.assertEqual(cat.legs(), 2)

    def test_dog_class(self):
        """Test case:
        * Dog's speak method should return 'arf'.
        * Dog's 'legs' method should return the output of Mammal's legs method multiplied by 2.
        """
        mammal = Mammal()
        dog = Dog()
        self.assertEqual(dog.speak(), 'arf')
        self.assertEqual(dog.legs(), mammal.legs()*2)

    def test_init_attr_not_accesible_when_preceded_by_double_underscore(self):
        """Test case:
        * test that illustrates an attribute defined in the `__init__` method of 'Mammal' is not
        accessible to Dog or Cat when preceded by a double-underscore, but an attribute
        preceded by a single-underscore or no underscore is.
        """
        mammal = Mammal()
        cat = Cat()
        dog = Dog()

        self.assertEqual(cat.info_type(), mammal.info_type())       # __type not accessible to Cat (is not able to overwrite it)
        self.assertNotEqual(cat.info_temp(), mammal.info_temp())    # _temp accessible to Cat (is able to overwrite it)
        self.assertNotEqual(cat.info_body(), mammal.info_body())    # body accessible to Cat (is able to overwrite it)

        self.assertEqual(dog.info_type(), mammal.info_type())       # __type not accessible to Dog (is not able to overwrite it)
        self.assertNotEqual(dog.info_temp(), mammal.info_temp())    # _temp accessible to Dog (is able to overwrite it)
        self.assertNotEqual(dog.info_body(), mammal.info_body())    # body accessible to Dog (is able to overwrite it)

    def test_dog2_class(self):
        """Test case: Should behave like Dog's class
        * Dog's speak method should return 'arf'.
        * Dog's 'legs' method should return the output of Mammal's legs method multiplied by 2.
        """
        dog = Dog()
        dog2 = Dog2()
        self.assertEqual(dog2.speak(), dog.speak())
        self.assertEqual(dog2.legs(), dog.legs())

        # Option with no inheritance.
        dog3 = Dog3()
        self.assertEqual(dog3.speak(), dog.speak())
        self.assertEqual(dog3.legs(), dog.legs())


class GraphsTestCase(unittest.TestCase):
    def test_duplicate_node(self):
        """Test case: Each node is unique
        """
        g = Graph()
        g.addNode(Node('A'))
        with self.assertRaises(ValueError) as context:
            g.addNode(Node('A'))
        self.assertTrue('Duplicate node' in context.exception)

    def test_node_type_Node(self):
        """Test case: Check that node is a Node object
        """
        g = Graph()
        with self.assertRaises(TypeError) as context:
            g.addNode('A')
        self.assertTrue('A is not of type Node' in context.exception)

    def test_add_node(self):
        """Test case: Check the node is in graph.nodes
        """
        g = Graph()
        g.addNode(Node('A'))
        self.assertIn('A', g.nodes)

    def test_duplicate_edge(self):
        g = Graph()
        g.addNode(Node('A'))
        g.addNode(Node('B'))
        g.addEdge(Edge(Node('A'), Node('B')))  # A --> B
        with self.assertRaises(ValueError) as context:
            g.addEdge(Edge(Node('A'),Node('B')))
        self.assertTrue('The edge (Node: A, Node: B) is already in the graph' in context.exception)

    def test_edge_added_from_to__non_existing_node(self):
        """Test case: Check when an edge is added from or to a non existing node
        """
        g = Graph()
        g.addNode(Node('A'))
        g.addNode(Node('B'))
        with self.assertRaises(ValueError) as context:
            g.addEdge(Edge(Node('A'), Node('D')))  # A --> D
            g.addEdge(Edge(Node('D'), Node('A')))  # D --> A
        self.assertTrue('Node: A and Node: D must be in the graph' in context.exception)

    def test_add_edge(self):
        g = Graph()
        n1 = Node('A')
        n2 = Node('B')
        g.addNode(n1)
        g.addNode(n2)
        g.addEdge(Edge(n1, n2))  # A --> B
        self.assertIn(n2, g.edges[n1])
        self.assertEqual([], g.edges[n2])

    def test_edge_type_Edge(self):
        """Test case: Check that edge is a Edge object
        """
        g = Graph()
        with self.assertRaises(TypeError) as context:
            g.addEdge(('A','B'))

    def test_method_has_key_of_Graph(self):
        """Test case:
        * check that node is a Node object
        * if the key is available in the dict, return True
        """
        g = Graph()
        with self.assertRaises(TypeError) as context:
            g.has_key('A')
        self.assertTrue('A is not of type Node' in context.exception)

        n1 = Node('A')
        g.addNode(n1)
        self.assertTrue(g.has_key(n1))

    def test_method_getitem_of_Graph(self):
        """Test case:
        * Nodes A, B. C, D. Neighbors of A: B and D
        """
        g = Graph()
        g.addNode(Node('A'))
        g.addNode(Node('B'))
        g.addNode(Node('C'))
        g.addNode(Node('D'))
        g.addEdge(Edge(Node('A'), Node('B')))  # A --> B
        g.addEdge(Edge(Node('A'), Node('D')))  # A --> D
        self.assertIn(Node('B'), g[Node('A')])
        self.assertIn(Node('D'), g[Node('A')])

    def test_method_eq_of_Node(self):
        n = Node('A')
        n1 = Node('A')
        self.assertTrue(n == n1)

    def test_method_hash_of_Node(self):
        n = Node('A')
        n1 = Node('A')
        self.assertEqual(hash(n), hash(n1))

    def test_equality_of_find_all_paths(self):
        """Test case:
        * Tests that uses the same `find_all_paths` method to show that the two graph
        representations are interchangeable.
        :graph: guido representation
        """
        g = test_graph()
        n1 = Node('A')
        n2 = Node('D')
        self.assertEqual(find_all_paths(g, n1, n2), find_all_paths(graph, 'A', 'D'))

    def test_equality_of_find_shortest_path(self):
        """Test case:
        * Tests that uses the same `find_shortest_path` method to show that the two graph
        representations are interchangeable.
        :graph: guido representation
        """
        g = test_graph()
        n1 = Node('A')
        n3 = Node('C')
        self.assertEqual(find_shortest_path(g, n1, n3), find_shortest_path(graph, 'A', 'C'))


class IgraphsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
            graph = {'A': ['B', 'C'],
                   'B': ['C', 'D'],
                   'C': ['D'],
                   'D': ['C'],
                   'E': ['F'],
                   'F': ['C']}

        """
        cls.vertice = 6
        cls.edges = [(0,1),(0,2), (1,2), (1,3), (2,3), (3,2), (4,5), (5,2)]
        cls.g = create_graph(cls.vertice,cls.edges)
        # square graph
        cls.g2 = create_graph(4, [(0,1), (0,2), (1,0), (1,3), (2,0), (2,3), (3,1), (3,2)])

    def test_create_guido_graph(self):
        """Test case:
        * Nodes are added
        * Edges are added

        """
        for v in self.g.vs:
            self.assertIn(v.index,range(self.vertice))
        self.assertItemsEqual(self.g.get_edgelist(),self.edges)

    def test_highest_degree_node(self):
        # node C
        self.assertEqual([2], highest_degree_node(self.g))

    def test_average_degree(self):
        # sum([2, 3, 5, 3, 1, 2])/leng(6)
        self.assertEqual(2.6666666666666665, average_degree(self.g))

    def test_is_bipartite(self):
        self.assertFalse(is_bipartite(self.g))
        self.assertTrue(is_bipartite(self.g2))

    def test_graph_diameter(self):
        self.assertEqual(3, graph_diameter(self.g))
        self.assertEqual(2, graph_diameter(self.g2))

if __name__ == '__main__':
    unittest.main()
