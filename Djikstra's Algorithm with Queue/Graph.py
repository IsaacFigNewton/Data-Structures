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

    # the getPath function should take the vertInfo list and the index of the current vertex to check
    # and should call itself recursively, getting the previous vertices until the startingVertex,
    # which has a previous node of 0, is reached, and then return a list of the vertices


    #problem somewhere in here methinks
    def getPath(self, pathInfoList, vertIndex, startVertex):
        orphanVertexPhrase = "oh no, cringe"
        previousVert = pathInfoList[vertIndex][1]
        print("previousVert: " + str(previousVert))

        #termination condition
        #if there is no previous node linked to the current one
        # (the distance of the path from startVertex to anywhere is only 0 if the previous vertex was itself)
        if (pathInfoList[vertIndex][2] == 0):
            #return nothing because the next vertex up the recursion loop
            # to be returned will be the startingVertex
            return []

        #otherwise, if there is a previous vertex along the path from startVertex to the current one
        else:
            #if there is no previousVert, it means that there's no path to it from startVert
            if (previousVert is None):
                print("No path was found between vertex " + str(startVertex.getId()) + " and vertex " + str(vertIndex))
                return [orphanVertexPhrase]#None]
            else:
                #get the path of all nodes starting at the startingVertex before the current one
                previousVertPath = self.getPath(pathInfoList, previousVert.getId(), startVertex)

                #if the current vertex isn't an orphan, add the current vertex to the path list
                if (previousVertPath != [orphanVertexPhrase]):
                    previousVertPath += [previousVert]

                #return the path from the startVertex to the previous vertex plus the previous vertex
                return previousVertPath

    def getShortestPaths(self, pathInfoList, startVertex):
        #when all the vertices accessible from the startingNode have been chequed,
        #create a 2D list of paths
        shortestPaths = [[]] * self.numVertices

        #create the lists of vertex objects that make up the path
        for vertIndex in self.vertList:
            print("current vertex: " + str(vertIndex))
            print("shortest paths: " + str(shortestPaths))
            #the .append is to add the current vertice to the end of the list
            shortestPaths[vertIndex] = self.getPath(pathInfoList, vertIndex, startVertex) + [self.getVertex(vertIndex)]

            print("")

        return shortestPaths

    #returns the shortest paths from every other vertex to the input (target) vertex
    def shortest_path(self, startVertex):
        #vertex checked state, previous vertice that can be traversed to reach vertex from startVertex,
        #distance to vertex
        pathInfoList = [(False, None, 10**100) for vertex in self.vertList]

        #initialize the queue
        queue = queue_array.QueueArray(self.numVertices)

        #the starting vertex has a path to itself of length 0
        pathInfoList[startVertex.id] = (True, startVertex, 0)

        #add the starting vertex to the queue
        queue.enqueue(startVertex)

        #check everything in the graph by adding stuff to the queue and checking everything in that
        while (not queue.is_empty()):
            #remove the current vertex from the eueuque and set the currentVertex variable to it
            currentVertex = queue.dequeue()

            #checked state is updated to True, to indicate that it has/is being checked
            # and shouldn't be re-added to the queue
            pathInfoList[currentVertex.getId()] = (True, pathInfoList[currentVertex.getId()][1], pathInfoList[currentVertex.getId()][2])

            #check all the connections of the starting vertex
            for nextVert in currentVertex.connectedTo:
                #if the next vertice hasn't been checked already
                if (not pathInfoList[nextVert.id][0]):
                    #add nextVert to the queue
                    queue.enqueue(nextVert)

                #the combined weight of the path from nextVert to the currentVertex and
                # that of the currentVertex
                newCost = currentVertex.connectedTo.get(nextVert) + pathInfoList[currentVertex.getId()][2]
                oldCost = pathInfoList[nextVert.getId()][2]

                #if a shorter path is found
                if (newCost < oldCost):
                    #update pathInfoList path info for the nodes found;
                    #previous vertice is set to currentVertex
                    # and path cost is updated from oldCost value to newCost
                    pathInfoList[nextVert.id] = (pathInfoList[nextVert.getId()][0], currentVertex, newCost)

        print("")
        self.printVertInfo(pathInfoList)

        """
        return a list of formatted like [(vertex object,
        [list of vertex objects that form the shortest path
        from/including the startingVertex to/including the current vertex],
        cost of traversing the shortest path)]
        """
        shortestPaths = self.getShortestPaths(pathInfoList, startVertex)

        return [(self.getVertex(vertexIndex), shortestPaths[vertexIndex], pathInfoList[vertexIndex][2]) for vertexIndex in self.vertList]

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

            print(toPrint + "\n")

    def printVertInfo(self, list):
        printableList = [None] * len(list)
        for i in range(len(list)):
            if (list[i][1] != None):
                if (isinstance(list[i][1], Vertex.Vertex)):
                    printableList[i] = (list[i][0], list[i][1].getId(), list[i][2])
                else:
                    printableList[i] = list[i]

        print("has been checked\tid of previous vert\t\tcumulative weight of path")

        printableList = str(printableList)
        string = ""
        for character in printableList:
            if (character == ","):
                string += ",\t\t\t\t\t"
            elif (character == "("):
                string += "\n("
            else:
                string += str(character)

        print(string + "\n")

    def printVertPathInfo(self, list, printIds=True):
        printableList = list
        for i in range(len(list)):
            if (list[i][1] != None):
                #default
                currentVert = list[i][0]
                vertPath = list[i][1]

                #if you want to print the vertice numbers instead of their addresses
                if (printIds):
                    #set the current vertice to its id
                    currentVert = currentVert.getId()

                    # create the list of vertice numbers if you want to print the vertex ids instead of the addresses
                    vertPath = []
                    for vert in list[i][1]:
                        if (isinstance(vert, Vertex.Vertex)):
                            vertPath += [vert.getId()]
                        else:
                            vertPath += [vert]

                #if the last element in the path list is a vertex object, print it
                if (isinstance(list[i][1][-1], Vertex.Vertex)):
                    printableList[i] = (currentVert, vertPath, list[i][2])
                else:
                    printableList[i] = list[i]

        print("current vertex\t\t\t\t\t\t\tpath from firstVert to current vert"
              "\t\t\t\t\tcumulative weight of path")

        printableList = str(printableList)
        string = ""
        for character in printableList:
            if (character == "["):
                string += "\t\t\t\t\t\t\t\t\t\t["
            elif (character == "]"):
                string += "]\t\t\t\t\t\t\t\t\t\t"
            elif (character == "("):
                string += "\n("
            else:
                string += str(character)

        print(string + "\n")