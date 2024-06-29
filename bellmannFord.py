class BellmannFord:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def bellmann(self, sorce):
        distance = [float('inf')] * self.vertices
        distance[sorce] = 0
        
        for _ in range(self.vertices - 1):
            for u, v, w in self.graph:
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
        
        for u, v, w in self.graph:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                print('Negative cycle detected')
                return
        
        self.printSolution(distance)
    
    def printSolution(self, distance):
        for i in range(self.vertices):
            print(f"{i} - {distance[i]}")


g = BellmannFord(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.bellmann(0)