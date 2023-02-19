from collections import defaultdict

def has_cycle(graph):
    """
    Check if the given graph has cycle or not using Depth First Search (DFS)
    """
    visited = defaultdict(int)
    
    def dfs(node):
        visited[node] = 1
        for neighbor in graph[node]:
            if visited[neighbor] == 1:
                # Cycle found
                return True
            elif visited[neighbor] == 0:
                if dfs(neighbor):
                    return True
        visited[node] = 2
        return False
        
    for node in graph:
        if visited[node] == 0:
            if dfs(node):
                return True
                
    return False

graph = defaultdict(list)
graph[1] = [2, 3]
graph[2] = [4, 5]
graph[3] = [4]
graph[4] = [5]
graph[5] = []


print(graph)
print(has_cycle(graph))
