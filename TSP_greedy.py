class TSP:
    def __init__(self, graph, start_state):
        self.graph = graph
        self.best_cost = float('inf')
        self.best_path = []
        self.start_state = start_state
    
    def greedy_approach(self):
        visited = [self.start_state]
        total_cost = 0
        
        for _ in range(len(self.graph) - 1):
            current_vertex = visited[-1]
            next_vertex, cost = self.nearest_vertex(current_vertex, visited)
            total_cost += cost
            visited.append(next_vertex)
        
        total_cost += self.graph[visited[-1]][self.start_state]
        visited.append(self.start_state)
        return visited, total_cost
    
    def nearest_vertex(self, vertex, visited):
        nearest = {node: cost for node, cost in self.graph[vertex].items() if node not in visited and cost != 0}
        nearest_vertex = min(nearest, key=nearest.get)
        return nearest_vertex, nearest[nearest_vertex]


# Example usage
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

tsp = TSP(graph, 'D')
print(tsp.greedy_approach())
