class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.rank[root_u] += 1
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []
    
    def add_edge(self, source, dest, weight):
        self.edges.append((source, dest, weight))
    
    def kruskal_mst(self):
        mst_edges = []
        ds = DisjointSet(self.num_vertices)
        self.edges.sort(key=lambda x: x[2])
        
        for edge in self.edges:
            u, v, weight = edge
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                mst_edges.append(edge)
        
        return mst_edges, ds.parent, ds.rank


# Example usage:
g = Graph(5)  # Number of vertices

# Adding edges with weights using add_edge method
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.add_edge(2, 4, 8)
g.add_edge(3, 4, 12)

mst, parent, rank = g.kruskal_mst()
for edge in mst:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")

print(parent)
print(rank)
