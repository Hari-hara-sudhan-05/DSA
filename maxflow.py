from collections import deque
class MaxFlow:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
    def bfs(self, s, t, parent):
        visited = [False] * self.ROW
        queue = deque([s])
        visited[s] = True
        while queue:
            u = queue.popleft()
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0
        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            max_flow += path_flow
        return max_flow


# Example usage
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

max_flow = MaxFlow(graph)
source = 0
sink = 5

print("The maximum possible flow is %d" % max_flow.ford_fulkerson(source, sink))
