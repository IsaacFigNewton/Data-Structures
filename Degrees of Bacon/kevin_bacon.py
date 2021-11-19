import Graph
import Vertex


def bacon_number(g, actor):
    """Takes an actor name and returns their Bacon number"""
    shortestPaths = g.shortest_path(g.getVertex('Kevin Bacon'))
    actorEntry = g.getEntryFromPathsListWithKey(shortestPaths, actor)
    return actorEntry[2]

def bacon_degree(g, actor):
    """Takes an actor name and returns the shortest path to Kevin Bacon"""
    shortestPaths = g.shortest_path(g.getVertex('Kevin Bacon'))
    actorEntry = g.getEntryFromPathsListWithKey(shortestPaths, actor)
    shortestPath = actorEntry[1]

    #replace all vertice objects with the respective actors' names
    for i in range(len(shortestPath)):
        shortestPath[i] = shortestPath[i].getId()

    return shortestPath

def bacon_actors_with_degree(g, n):
    """Returns all actors with degree n to Kevin Bacon"""
    shortestPaths = g.shortest_path(g.getVertex('Kevin Bacon'))

    #go through the list of actors and their paths to Bacon
    # to compile a list of actors with a specific Bacon number
    actorNames = []
    for entry in shortestPaths:
        if (entry[2] == n):
            #add the name of the actor with the indicated path length to the list of actorNames
            actorNames.append(entry[0].getId())

    return actorNames

def highest_bacon(g):
    """Returns the actor(s) with the highest Bacon degree"""
    shortestPaths = g.shortest_path(g.getVertex('Kevin Bacon'))

    furthestActorEntries = [(None, None, -1)]
    for entry in shortestPaths:
        #if there's a larger furthest actor entry
        if (entry[2] > furthestActorEntries[0][2]):
            #overwrite the current list of largest actors with a new list,
            # with the current largest as the sole element
            furthestActorEntries = [entry]

        #otherwise, if there's another actor with the same furthest distance
        elif (entry[2] == furthestActorEntries[0][2]):
            #add the current entry to the list
            furthestActorEntries.append(entry)

    #replace the entries in the list of furthest actors with their names
    for i in range(len(furthestActorEntries)):
        furthestActorEntries[i] = furthestActorEntries[i][0].getId()

    #return the list of the furthest actors' names
    return furthestActorEntries

def any_actors_degree(g, actor1, actor2):
    """A more general function to return the path length between any two actors"""
    shortestPaths = g.shortest_path(g.getVertex(actor1))
    actorEntry = g.getEntryFromPathsListWithKey(shortestPaths, actor2)
    return actorEntry[2]

"""
Code to build the example graph:
"""

g = Graph.Graph()
g.addVertex('Kevin Bacon')
g.addVertex('Tom Hanks')
g.addVertex('Bill Paxton')
g.addVertex('Paul Herbert')
g.addVertex('Yves Aubert')
g.addVertex('Shane Zaza')
g.addVertex('Seretta Wilson')
g.addVertex('Meryl Streep')
g.addVertex('John Beluci')
g.addVertex('Kathleen Quinlan')
g.addVertex('Donald Sutherland')
g.addVertex('Lloyd Bridges')
g.addVertex('Grace Kelly')
g.addVertex('Nicole Kidman')
g.addVertex('Patrick Allen')
g.addVertex('Glenn Close')
g.addVertex('John Gielgud')
g.addVertex('Vernon Dobtcheff')
g.addVertex('Kate Winslet')

g.addBiEdge('Kevin Bacon', 'Tom Hanks')
g.addBiEdge('Kevin Bacon', 'John Beluci')
g.addBiEdge('Kevin Bacon', 'Meryl Streep')
g.addBiEdge('Kevin Bacon', 'Donald Sutherland')
g.addBiEdge('Kevin Bacon', 'Bill Paxton')
g.addBiEdge('Kevin Bacon', 'Kathleen Quinlan')
g.addBiEdge('Tom Hanks', 'Kathleen Quinlan')
g.addBiEdge('Tom Hanks', 'Bill Paxton')
g.addBiEdge('Tom Hanks', 'Paul Herbert')
g.addBiEdge('Tom Hanks', 'Yves Aubert')
g.addBiEdge('Tom Hanks', 'Shane Zaza')
g.addBiEdge('Tom Hanks', 'Seretta Wilson')
g.addBiEdge('Tom Hanks', 'Lloyd Bridges')
g.addBiEdge('Lloyd Bridges', 'Grace Kelly')
g.addBiEdge('Donald Sutherland', 'Patrick Allen')
g.addBiEdge('Donald Sutherland', 'Nicole Kidman')
g.addBiEdge('Donald Sutherland', 'Vernon Dobtcheff')
g.addBiEdge('Nicole Kidman', 'Glenn Close')
g.addBiEdge('Nicole Kidman', 'John Gielgud')
g.addBiEdge('Bill Paxton', 'Kate Winslet')
g.addBiEdge('Patrick Allen', 'John Gielgud')
g.addBiEdge('Nicole Kidman', 'John Gielgud')
g.addBiEdge('Vernon Dobtcheff', 'John Gielgud')

#use Kevin Bacon as the starting vertex
shortestPaths = g.shortest_path(g.getVertex('Kevin Bacon'))
g.printVertPathInfo(shortestPaths)
print("")

#run tests here
actor = "Kate Winslet"
n = 3
actor1 = "Kate Winslet"
actor2 = "Lloyd Bridges"
print("Bacon number of Kate Winslet: " + str(bacon_number(g, actor)))
print("Path between Bacon and Kate Winslet: " + str(bacon_degree(g, actor)))
print("Actor/s with Bacon number of 3: " + str(bacon_actors_with_degree(g, n)))
print("Actor/s with the highest Bacon number: " + str(highest_bacon(g)))
shortestPaths = g.shortest_path(g.getVertex('Kate Winslet'))
g.printVertPathInfo(shortestPaths)
print("Path length between Kate Winslet and Lloyd Bridges: " + str(any_actors_degree(g, actor1, actor2)))