class AttackGraph:
    def __init__(self):
        self.graph = {}
    def add_node(self, name: str):
        if name not in self.graph:
            self.graph[name] = []
        else:
            return None  
    def add_edge(self, src: str, dst: str, cost: float):
        if src in self.graph:
            self.graph[src].append([dst, cost])
        else:
            return None    
    def neighbors(self, name: str) -> list: 
        if name in self.graph:
            return self.graph[name]
        else:
            return []
    def has_cycle(self) -> bool:
        color = {}
        white = "WHITE"
        gray = "GRAY"
        black = "BLACK"
        for name in self.graph.keys():
            color[name] = white 
        def dfs(name):
            color[name] = gray
            for neighbor in self.neighbors(name):
                if color[neighbor[0]] == gray:
                    return True
                if  color[neighbor[0]] == white:
                    if dfs(neighbor[0]):
                        return True
            color[name] = black
            return False
        for name in color:
            if color[name] == white:
                if dfs(name):
                    return True
        return False  
    def topological_sort(self) -> list: 
        in_degree = {}  
        queue = []
        result = []
        for name in self.graph:
            in_degree[name] = 0
        for name in self.graph:
            for neighbor in self.neighbors(name):
                in_degree[neighbor[0]] += 1
        for name in in_degree:
            if in_degree[name] == 0:
                queue.append(name)
        while len(queue)  > 0:
            node = queue.pop(0)
            result.append(node) 
            for neighbor in self.neighbors(node):
                in_degree[neighbor[0]] -= 1
                if in_degree[neighbor[0]] == 0:
                    queue.append(neighbor[0])
        if len(result) != len(self.graph):
            raise ValueError("cycle detected")
        else:
            return result
    def cheapest_path(self, src: str, dst: str) -> tuple:
        dist = {}
        prev = {}
        for node in self.graph:
            dist[node] = float("infinity")
            prev[node] = None
        dist[src] = 0
        unvisited = set(self.graph.keys())
        path = []
        while unvisited:
            current = None
            for node in unvisited:
                if current is None or dist[current] > dist[node]:
                    current = node
            unvisited.remove(current)
            for neighbor in self.neighbors(current):
                new_dist = dist[current] + neighbor[1]
                if new_dist < dist[neighbor[0]]:
                    dist[neighbor[0]] = new_dist
                    prev[neighbor[0]] = current
        if dist[dst] == float("infinity"):
            raise ValueError
        current = dst
        while current is not None:
            path.append(current)
            current = prev[current]
        path.reverse()
        return (dist[dst],path)

if __name__ == "__main__":
    
    g2 = AttackGraph()
    for n in ['A', 'B', 'C']:
        g2.add_node(n)
    g2.add_edge('A', 'B', 1.0)
    g2.add_edge('B', 'C', 1.0)
    g2.add_edge('C', 'A', 1.0)
    print("Injection 1 has_cycle:", g2.has_cycle())  
    try:
        g2.topological_sort()
    except ValueError as e:
        print(f"Injection 1 topological_sort raised ValueError: {e}")  


    g3 = AttackGraph()
    g3.add_node('X')
    g3.add_node('Y')
    try:
        g3.cheapest_path('X', 'Y')
    except ValueError:
        print("Injection 2 cheapest_path raised ValueError: no path X->Y")  

  
    g4 = AttackGraph()
    g4.add_node('A')
    g4.add_node('B')
    g4.add_edge('A', 'B', 1.0)
    g4.add_edge('A', 'B', 0.1)
    print("Injection 3 duplicate edge cheapest_path:", g4.cheapest_path('A', 'B'))  

  
    g5 = AttackGraph()
    g5.add_node('A')
    g5.add_edge('A', 'A', 0.0)
    print("Injection 4 self-loop has_cycle:", g5.has_cycle())  
