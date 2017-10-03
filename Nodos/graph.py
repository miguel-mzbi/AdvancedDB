import csv
import collections

class Node(object):
        def __init__(self, id):
            self.id = id
            self.pageRank = 0.0
            self.adj = set()
            self.adjInv = set()

        def setC(self, c):
            self.c = c

        def addAdjacent(self, adjacent):
            self.adj.add(adjacent)

        def addAdjacentInv(self, adjacent):
            self.adjInv.add(adjacent)

        def __str__(self):
            return str(self.id)

        def __hash__(self):
            return hash(self.id)

        def __repr__(self):
            return str(self)

class Graph(object):
    
    def __init__(self, nodesList = None):
        self.nodes = nodesList

    def __init__(self, edgesPath = None):
        self.nodes = {}
        if edgesPath != None:
            with open(edgesPath) as csvfile:
                csvfile.readline()
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    n = row[0]
                    self.addVertex(n)
                    self.addEdge(n, row[1])

    def vertices(self):
        return [self.nodes]

    def addVertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = Node(vertex)

    def edges(self):
        return list(self.generateEdges())

    def addEdge(self, origin, destination):
        if origin not in self.nodes:
            self.addVertex(origin)
        if destination not in self.nodes:
            self.addVertex(destination)

        origin = self.nodes[origin]
        origin.addAdjacent(destination)

        destination = self.nodes[destination]
        destination.addAdjacentInv(origin)

    def generateEdges(self):
        edges = []
        for vertex in self.nodes:
            for adjacent in self.nodes[vertex].adj:
                if {vertex, adjacent} not in edges:
                    edges.append({vertex, adjacent})
        return edges

    def BFS(self, start):
        seen, queue = set(), [start]
        count = 0
        countLvl = 1
        level = 1
        while queue:
            vertex = queue.pop(0)
            if vertex not in seen:
                if countLvl > 0:
                    count += len(self.nodes[vertex].adj - seen)
                    countLvl -= 1
                    if vertex == start:
                        print("Level: " + str(level))
                        level += 1
                elif countLvl == 0:
                    print("Level: " + str(level))
                    level += 1
                    countLvl = count -1
                    count = 0
                print(vertex)
                seen.add(vertex)
                queue.extend(self.nodes[vertex].adj - seen)
        return seen

    def DFS(self, start):
        seen, stack, lvlStack = set(), [start], [1]
        level = 1
        prvLevel = 0
        while stack:
            vertex = stack.pop()
            level = lvlStack.pop()
            if vertex not in seen:
                
                if prvLevel != level:
                    print("Level: " + str(level))
                    prvLevel = level
                
                print(vertex)
                seen.add(vertex)

                stack.extend(self.nodes[vertex].adj() - seen)

                levels = [level+1] * len(self.nodes[vertex].adj - seen)
                lvlStack.extend(levels)
        return seen

    def setPageRankAll(self, prob):
        for node in self.nodes:
            self.nodes[node].pageRank = self.auxPageRankAll(node, prob)
            print("ID: " + str(node) + " - PR: " + str(self.nodes[node].pageRank))

    def auxPageRankAll(self, vertex, prob):
        toReturn = 1-prob
        node = self.nodes[vertex]
        accum = 0.0
        for pointingAtThis in node.adjInv:
            accum += pointingAtThis.pageRank / len(pointingAtThis.adj)
        toReturn += prob*accum
        return toReturn

    def __str__(self):
        res = "Vertices: "
        for k in self.nodes.keys():
            res += str(k) + " "
        res += "\nEdges: "
        for edge in self.generateEdges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":
    
    graph = Graph('Esa+Nasa EDGES.csv')
    #print(graph.vertices())
    #print(graph.generateEdges())
    #print("~~~~~~~~~~BFS~~~~~~~~~~")
    #print("Start Node: 79119377085 ")
    #graph.BFS('79119377085')
    #print("~~~~~~~~~~DFS~~~~~~~~~~")
    #print("Start Node: 79119377085 ")
    #graph.DFS('79119377085')
    for i in range(2):
        print("~~~~~~~~~~ Round " + str(i) + " ~~~~~~~~~~")    
        graph.setPageRankAll(0.85)