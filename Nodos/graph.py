import csv
import collections

class Graph(object):
    
    def __init__(self, graphDict = None):
        if graphDict == None:
            graphDict = {}
        self.graphDict = graphDict

    def __init__(self, edgesPath = None):
        if edgesPath == None:
            graphDict = collections.defaultdict(set)
        else:
            graphDict = collections.defaultdict(set)
            with open(edgesPath) as csvfile:
                csvfile.readline()
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    graphDict[row[0]].add(row[1])

        self.graphDict = graphDict

    def vertices(self):
        return list(self.graphDict.keys())

    def addVertex(self, vertex):
        if vertex not in self.graphDict.keys():
            self.graphDict[vertex] = []

    def edges(self):
        return list(self.generateEdges())

    def addEdge(self, origin, destination):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if origin in self.graphDict.keys() and destination in self.graphDict.keys():
            self.graphDict[origin].add(destination)
        else:
            self.graphDict[origin] = set([vertex2])

    def generateEdges(self):
        edges = []
        for vertex in self.graphDict.keys():
            for adjacent in self.graphDict[vertex]:
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
                    count += len(self.graphDict[vertex] - seen)
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
                queue.extend(self.graphDict[vertex] - seen)
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

                stack.extend(self.graphDict[vertex] - seen)

                levels = [level+1] * len(self.graphDict[vertex] - seen)
                lvlStack.extend(levels)
        return seen

    def __str__(self):
        res = "Vertices: "
        for k in self.graphDict.keys():
            res += str(k) + " "
        res += "\nEdges: "
        for edge in self.generateEdges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":
    
    graph = Graph('Esa+Nasa EDGES.csv')
    #print(graph.vertices())
    #print(graph.generateEdges())
    print("~~~~~~~~~~BFS~~~~~~~~~~")
    print("Start Node: 79119377085 ")
    graph.BFS('79119377085')
    print("~~~~~~~~~~DFS~~~~~~~~~~")
    print("Start Node: 79119377085 ")
    graph.DFS('79119377085')

