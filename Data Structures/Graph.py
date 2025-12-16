class Graph:
    def __init__(self):
        self.adjList = {}

    def printGraph(self):
        for vertex in self.adjList:
            print(vertex,':', self.adjList[vertex])

    def addVertex(self, vertex):
        if vertex not in self.adjList.keys():
            self.adjList[vertex] = []
            return True
        return False

    def addEdge(self, v1, v2):
        if not v1 in self.adjList.keys() or not v2 in self.adjList.keys():
            return False
        else:
            self.adjList[v1].append(v2)
            self.adjList[v2].append(v1)
            return True

    def removeEdge(self, v1, v2):
        if not v1 in self.adjList.keys() or not v2 in self.adjList.keys():
            return False
        else:
            try:            
                self.adjList[v1].remove(v2)
                self.adjList[v2].remove(v1)
            except ValueError:
                pass
            return True

    def removeVertex(self, vertex):
        if vertex in self.adjList.keys():
            for otherVertex in self.adjList[vertex]:
                self.adjList[otherVertex].remove(vertex)
            del self.adjList[vertex]
            return True
        return False
      
      
         
graph = Graph()
graph.addVertex('A')
graph.addVertex('B')
graph.addVertex('C')
graph.addVertex('D')


graph.addEdge('A', 'B')
graph.addEdge('A', 'C')
graph.addEdge('A', 'D')
graph.addEdge('B', 'D')
graph.addEdge('C', 'D')
graph.removeVertex('D')
graph.printGraph()
