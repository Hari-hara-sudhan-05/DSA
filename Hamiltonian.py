class Hamiltonian:
    def __init__(self, vertices):
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.v = vertices
    
    def is_safe(self, v, pos, path):
        return self.graph[path[pos - 1]][v] == 1 and v not in path
    
    def hamiltonian_util(self, path, pos):
        if pos == self.v:
            return self.graph[path[pos - 1]][path[0]] == 1
        
        for v in range(self.v):
            if self.is_safe(v, pos, path):
                path[pos] = v
                if self.hamiltonian_util(path, pos + 1):
                    return True
                path[pos] = -1
        return False
    
    def hamiltoninan_circuit(self):
        path = [-1] * self.v
        path[0] = 0
        if not self.hamiltonian_util(path, 1):
            print('No')
            return False
        
        self.print_sol(path)
        return True
    
    def print_sol(self, path):
        print('yes')
        for v in path:
            print(v, end=" -> ")
        print(path[0])


g1 = Hamiltonian(5)
g1.graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

g1.hamiltoninan_circuit()