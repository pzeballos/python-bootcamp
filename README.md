Python Proficiency Test
==========================

Python codes for different concepts.


Introduction
------------

    1. Loops and Conditional Statements
    2. Basic Data Structure Manipulation
        * Sorting
        * List Comprehensions
        * Filtering
        * Generators
    3. Object Oriented Concepts
        * Classes / Models
        * Inheritance
        * Encapsulation
    4. Algorithms and Advanced Data Structures
        * Graphs
        * Graph Traversal
        * igraph


1. Loops And Conditional Statements
-----------------------------------
    1. Write function containing a loop that iterates over a range of values, 1-50. Return those values. 
    2. Write a function containing a loop that iterates over a range of values, 0-50, skipping every odd number. Return the unskipped values. Use 'continue' for this
    3. Write a function containing loop that iterates, generating random integers between 1 and 100, stopping when the returned number is 42. Return the numbers generated up to this point.

2. Basic Data Structure Manipulation
------------------------------------
    1. Write a function that sorts the numbers you generated in 1.3 in ascending order.
    2. Write a function that filters the numbers returned by the method implemented in 1.3 so they match 1.1
    3. Write a lambda function that returns the same output of 1.2
    4. Write a lambda function that returns a dictionary of the form `{0: 1, 1: 2, 2: 3, ..., 9: 10}`
    5. Write 1.1, 1.2, 1.3, 2.1, and 2.2 as generators.

3. Object Oriented Concepts
---------------------------
    1. Write a class called Mammal. 
        * Mammal should have a method called 'speak' that returns 'hello'.
        * Mammal should have a method called 'legs' that returns 2.
        * Allow the output of 'legs' to be overwritten by modifying the _legs attribute of the Mammal class.
    2. Write a class called Cat that inherits from Mammal.
        * Cat's speak method should return 'meow'. Don't define a speak method. Inherit it.
        * Cat's 'legs' method should return 2. Dont' define a 'legs' method. Inherit it.
    3. Write a class called Dog that inherits from Mammal.
        * Dog's speak method should return 'arf'
        * Define a method on Dog that overrides Mammal's legs method. It should return the output of Mammal's legs method multiplied by 2.
    4. Write a test that illustrates an attribute defined in the `__init__` method of 'Mammal' is not accessible to Dog or Cat when preceded by a double-underscore, but an attribute preceded by a single-underscore or no underscore is.. 
    5. Write a new Dog class called Dog2 that doesn't inherit from Mammal. It should behave the same way. 

4. Algorithms and Advanced Data Structures
------------------------------------------
Guido has a recommended method of creating basic directed graphs in Python: http://www.python.org/doc/essays/graphs/. (You'll find it implemented in guido.py).

    1. Write a class called Graph, Node, and Edge. The Graph should be able to contain Node and Edge objects that implements the same interface as guido's list and dict implementation:
        a) `for node in graph`
        b) `for node in graph[node_name]`
        c) `graph.has_key(node_name)`

       The benefit of this implementation is now Nodes and Edges can contain metadata we have immediate access to while not losing any of the functionality we've already got laying around in the find_all_paths and find_shortest_paths methods.

       Ensure the node object we're getting out of the iterators in 4.1 a) and 4.1 b) are instances of the Node class.

    2. Write tests that uses the same `find_all_paths` and `find_shortest_path` method to show the two graph representations are interchangeable. 
    3. Install igraph for Python. This might be helpful: http://hal.elte.hu/~nepusz/development/igraph/tutorial/tutorial.html
    4. Using the graph example (stored in the variable, graph) in guido.py write a function that uses igraph to output the highest degree node, the average degree, whether or not the graph is bipartite, and the diameter. Include comments that explains what each of these things mean.


Notes:
------
* To run the test `python -m unittest test` (In a future, if test grow, we can add a runtest.py,
but we don't have many files of test at the moment)
* To run graphs.py `python graphs.py` . To run igraphs.py `python igraphs.py`
