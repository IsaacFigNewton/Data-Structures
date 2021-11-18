import Graph
import Vertex


def bacon_number(g, actor):
    """Takes an actor name and returns their Bacon number"""


def bacon_degree(g, actor):
    """Takes an actor name and returns the shortest path to Kevin Bacon"""


def bacon_actors_with_degree(g, n):
    """Returns all actors with degree n to Kevin Bacon"""


def highest_bacon(g):
    """Returns the actor(s) with the highest Bacon degroo"""


def any_actors_degree(g, actor1, actor2):
    """A more general function to return the path length between any two actors"""


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

#run tests here
#use Kate Winslet as the starting vertex
shortestPaths = g.shortest_path(g.getVertex('Kate Winslet'))
g.printVertPathInfo(shortestPaths)