import unittest
import Vertex
import Graph
import random

class MyTestCase(unittest.TestCase):
    def test_djikstra(self):
        #instantiate stuff
        graph = Graph.Graph()
        startVertex = -1
        for i in range(10):
            #add vertex with key of i
            graph.addVertex(i)

            #add 2 random edges to the current node
            if (i > 0):
                #do i//2 as the lower bound to distribute edges more evenly
                graph.addEdge(i, random.randint(i // 2, i - 1), random.randint(0, 10))
                graph.addEdge(i, random.randint(i // 2, i - 1), random.randint(0, 10))

        #note:  the first and last vertices (ex: 0 and 9 in a set of 10 vertices)
        #       will always be endpoints with the first vertice having no outgoing edges and
        #       the last vertice having no incoming edges

        graph.printEdges()

        #print the shortest paths from every node to the start node
        #graph.printf(graph.shortest_path(graph.getVertex(9)))

        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
