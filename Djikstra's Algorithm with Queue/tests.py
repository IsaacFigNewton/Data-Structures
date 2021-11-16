import unittest
import Graph
import random

class MyTestCase(unittest.TestCase):
    def test_djikstra(self):
        #instantiate stuff
        graph = Graph.Graph()
        #startVertex = -1

        for i in range(10):
            #add vertex with key of i
            graph.addVertex(i)

        for i in range(graph.numVertices):
            #add 2 random edges to the current node
            nextVertexIndex = random.randint(0, graph.numVertices - 1)
            while (nextVertexIndex == i):
                nextVertexIndex = random.randint(0, graph.numVertices - 1)
            graph.addEdge(i, nextVertexIndex, random.randint(1, 10))

            nextVertexIndex = random.randint(0, graph.numVertices - 1)
            while (nextVertexIndex == i):
                nextVertexIndex = random.randint(0, graph.numVertices - 1)
            graph.addEdge(i, nextVertexIndex, random.randint(1, 10))

        graph.printEdges()

        #print the shortest paths from every node to the start node
        #do true or false to change whether it prints the addresses or the ids
        #(default is just ids)
        graph.printVertPathInfo(graph.shortest_path(graph.getVertex(1)))#, False)

        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
