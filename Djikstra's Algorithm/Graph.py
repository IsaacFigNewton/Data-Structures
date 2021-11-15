import Vertex
import queue_array

class Graph:
    def __init__(self):
        #a dictionary of vertice indices and their respective vertex objects
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex.Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        #if a vertex with id f isn't in the list of vertices, add it
        if f not in self.vertList:
            nv = self.addVertex(f)
        #if a vertex with id t isn't in the list of vertices, add it
        if t not in self.vertList:
            nv = self.addVertex(t)

        #add an edge between vertex f and vertex t
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def addAllNeighborVerticesToQueue(self, queue, vertice):
        neighbors = vertice.getConnections
        for neighbor in neighbors:
            #add the current vertice and the weight of its edge with the parent vertice
            #to the traversal queue as a tuple
            queue.enqueue(neighbor)

    #returns the shortest paths from every other vertex to the input (target) vertex
    def shortest_path(self, startVertex):
        """
        #vertex checked state, previous vertice that can be traversed to reach v from startVertex, distance to vertex
        pathInfoList = [(False, None, infinity) for vertex in self.vertList]

        #initialize the queue
        queue = queue(max number of paths in the graph)
        currentDistance

        #set the distance from the start vertex to 0
        startVertex.setDistance(0)

        #the starting vertex has a path to itself of length 0
        pathInfoList[startVertex.id] = (True, startVertex, 0)

        #add the starting vertex to the queue
        queue.enguueue(startVertex)

        #check everything in the graph by adding stuff to the queue and checking everything in that
        while (not queue.isEmpty()):

            #remove the current vertex from the eueuque and set the currentVertex variable to it
            currentVertex = queue.degueue(currentVertex)
            pathInfoList[currentVert.id] = (pathInfoList[currentVert.id] stuff,
                                                but vertex checked state is updated to True,
                                                to indicate that it has/is being checked and shouldn't be
                                                re-added to the queue

            #check all the connections of the starting vertex
            for nextVert in currentVertex.connectedTo:
                if (not nextVert has been checked (vertex checked state is False)):
                    #add nextVert to the queue
                    queue.enqueueueue(nextVert)

                newCost = the combined weight of the path from nextVert to the currentVertex and
                            that of the currentVertex
                oldCost = pathInfoList[nextVert.id][index of path cost]

                #if a shorter path is found
                if (newCost < oldCost):
                    #update pathInfoList path info for the nodes found
                    pathInfoList[nextVert.id] = (pathInfoList[nextVert.id] stuff,
                                                but previous vertice is set to currentVertex
                                                and path cost is updated from oldCost value to newCost value

        #when all the vertices accessible from the startingNode have been chequed,
            return a list of formatted like [(vertex object,
            [list of vertex objects that form the shortest path
            from/including the startingVertex to/including the current vertex],
            cost of traversing the shortest path)]

        #create a table of paths
        shortestPaths = [[] * len(self.vertList)]
        #create the lists of vertex objects that make up the path
        for vertIndex in range(len(pathInfoList)):

            #the getPath function should take the vertInfo list and the index of the current vertex to check
            #and should call itself recursively, getting the previous vertices until the startingVertex,
            #which has a previous node of 0, is reached, and then return a list of the vertices
            #the .append is to add the current vertice to the end of the list
            shortestPaths[vertIndex] = getPath(vertInfo, vertIndex).append(self.getVertex(vertIndex))

        listToReturn = [(vertex, [shortest path], path cost) for vertex in self.vertList]

        return listToReturn

        #not sure if prof. wants this but
        #when all the vertices accessible from the startingNode have been checked
            all the vertex checked states should be set to true, but if they aren't,
            the following could be used to detect that or find paths to all the nodes
        for vert in pathInfoList:
            #if a vertex hasn't been checked,
                select the first unchecked node and repeat Djikstra's algorithm there
            if (not vert[index of vert checked state]):
                print ("uh oh, not every node was accessible from the starting node,
                        \nso let's try it again somewhere else")
                #call djikstra recursively until all nodes have been checked?
                self.shortest_path(vert[index of vertex object])
                break
        """












        """
        #initialize the priority queue
        pq = PriorityQueue()
        #set the distance from the start vertex to 0
        startVertex.setDistance(0)
        #add all the vertices in the graph
        #and their distances from the start vertex to the priority queue
        pq.buildHeap([(v.getDistance(), v) for v in aGraph])
        #while there are still vertices to be checked
        while not pq.isEmpty():
            #set the current vertex to the nearest neighbor and remove it from the priority queue
            currentVert = pq.delMin()
            #for all neighbors of the nearest neighbor
            for nextVert in currentVert.getConnections():
                #set new distance to the current vertex's distance from the start vertex
                #plus the distance from the current vertex to the next neighbor
                newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
                #if the new distance is less than the next neighbor's distance from the start vertex
                if (newDist < nextVert.getDistance()):
                    #set the next neighbor's distance from the start vertex to the new distance
                    nextVert.setDistance(newDist)
                    #??
                    nextVert.setPred(currentVert)
                    #decreases the key value of the next neighbor to the new distance from the start vertex
                    pq.decreaseKey(nextVert, newDist)
        """

        """
        #list of paths and their aggregate costs, with indices representing the vertice number
        #10^100 because you can't have infinity in Python
        pathList = {([], 10 ** 100) * self.numVertices}

        traversalQueue = queue_array.QueueArray(len(self.vertList) ** len(self.vertList) - 1)
        traversalQueue.enqueue(startVertex)
        currentPath = queue_array.QueueArray(len(self.vertList))
        currentVertice = startVertex
        previousVertice = startVertex
        startVertex.setDistance(0)

        #set the path information for the start node
        currentPath.enqueue(currentVertice)
        pathList[currentVertice.getId()] = ([currentVertice], 0)

        #traverse the graph in breadth-first order using a queue
        #while there are still vertices and edges to visit/check in the graph
        while(not traversalQueue.isEmpty()):
            previousVertice = currentVertice
            currentVertice = neighborPriorityQueue.dequeue()



            # check every vertex object in the vertList
            # and update path information if the node checked is the current one being read
            for vertice in self.vertList:
                #if the current vertice is the same as the one being checked
                if(currentVertice == vertice):
                    #and the current path distance is less than its previous path distance
                    if (currentDistance < pathList[vertice.getId()][1]):
                        #update the shortest path information for the designated vertex
                        pathList[vertice.getId()] = (currentpath.items, currentDistance)
                    #break to save time by not checking the rest of the nodes
                    break

            #add all the neighboring vertices of the current node at the top of the heap
            #to the heap ([0] because the tuple returned by deleteMin() is a vertex object and its weight
            self.addAllNeighborVerticesToQueue(traversalQueue, currentVertice)



            #check all its neighbors' ids to see if they are the target
            for neighbor in vertice.getConnections():
                pathList[i] = ()

        #{(v1,[],0), (v2,[v1,v2], 2), (v3,[v1,v4,v3],3),
        #(v4,[v1,v4],1), (v5,[v1,v4,v5],3), (v6,[v1,v4,v7,v6],6), (v7,[v1,v4,v7], 5)}

        #mark every node as ‘visited’ when you examine it and add its adjacencies to the queue
        #(add a variable to the Vertex class to do that).

        #update the cost only if it is lower than the existing cost.
        """

    def printEdges(self):
        #for every vertex in the graph
        for vert in self.vertList:
            toPrint = "Vertex " + str(vert) + " points to:\t"

            #add the ids/edge weights of the next nodes (from the connectedTo dictionary)
            edges = self.getVertex(vert).connectedTo
            for nextVertKey in edges:
                toPrint += "vertex " + str(nextVertKey.getId()) + " with a weight of " + str(edges.get(nextVertKey)) + ", \n\t\t\t\t\t"

            #remove the last ", " from the string to return
            toPrint = toPrint[0:-8]

            print(toPrint)
            #print(self.getVertex(vert).connectedTo)

    def printf(self, list):
        string = "{\n"

        for i in range(len(list)):
            string += str(list[i]) + ", "

            #print elements in square-ish blocks
            if (i % (int)(len(list) ** 0.5) == 0):
                #remove the last 2 characters from the string being printed
                string = string[0: -2]
                string += "\n"

        string += "\n}"

        print(string)