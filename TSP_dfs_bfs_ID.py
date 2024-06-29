from collections import deque
class TSP:
    def __init__(self,graph,start_state):
        self.graph = graph
        self.start_state = start_state
        self.end_state = start_state
        self.best_cost = float('inf')
        self.best_pair = None
        self.all_cost = []
        self.all_path = []
        self.num_cities = list(self.graph.keys())

    def calculate_cost(self,path):
        cost = 0
        for i in range(len(path)-1):
            cost+=self.graph[path[i]][path[i+1]]
        cost+=self.graph[path[-1]][self.end_state]
        return cost

    def dfs(self):
        stack = [(self.start_state,[self.start_state])]

        while stack:
            current_city,current_path = stack.pop()
            if len(current_path)==len(self.num_cities):
                total_cost = self.calculate_cost(current_path)
                self.all_path.append(current_path[:]+[self.end_state])
                self.all_cost.append(total_cost)
                if total_cost < self.best_cost:
                    self.best_cost = total_cost
                    self.best_pair = current_path[:]+[self.end_state]

            else:
                for next_city in self.num_cities:
                    if next_city not in current_path:
                        stack.append((next_city,current_path+[next_city]))


    def bfs(self):
        queue = deque([(self.start_state,[self.start_state])])

        while queue:
            current_city,current_path = queue.popleft()
            if len(current_path)==len(self.num_cities):
                total_cost = self.calculate_cost(current_path)
                self.all_path.append(current_path[:] + [self.end_state])
                self.all_cost.append(total_cost)
                if total_cost < self.best_cost:
                    self.best_cost = total_cost
                    self.best_pair = current_path[:] + [self.end_state]
                continue


            for next_city in self.num_cities:
                if next_city not in current_path:
                    queue.append((next_city,current_path+[next_city]))

    def bfs_iterative(self,current_city,current_path,current_depth,max_depth):
        if current_depth==max_depth:
            total_cost = self.calculate_cost(current_path)
            self.all_path.append(current_path[:] + [self.end_state])
            self.all_cost.append(total_cost)
            if total_cost < self.best_cost:
                self.best_cost = total_cost
                self.best_pair = current_path[:] + [self.end_state]
            return
        for next_city in self.num_cities:
            if next_city not in current_path:
                self.bfs_iterative(next_city,current_path+[next_city],current_depth+1,max_depth)

    def iterative_deepening(self):
        depth = len(self.num_cities)-1
        while self.best_cost ==  float('inf'):
            self.bfs_iterative(self.start_state,[self.start_state],0,depth)
            depth+=1

    def findAllSolution(self):
        # self.dfs()
        self.bfs()
        # self.iterative_deepening()
        return self.all_path,self.all_cost,self.best_pair,self.best_cost

if __name__ == '__main__':
    graph = {
        'A': {'A': 0,'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }
    start_state = 'A'
    end_state = 'A'
    ts = TSP(graph,start_state)
    all_path,all_cost,best_path,best_cost = ts.findAllSolution()
    for path,cost in zip(all_path,all_cost):
        print('Path',path)
        print('Cost',cost)

    print('Best cost and path is')
    print(best_path,best_cost)