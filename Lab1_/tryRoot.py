from collections import defaultdict

def can_reach_all_nodes(graph, node):
    # Define a recursive function to perform DFS and keep track of visited nodes
    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    # Initialize an empty set to keep track of visited nodes
    visited = set()

    # Perform DFS starting from the given node
    dfs(node, visited)

    # Check if the set of visited nodes is the same as the set of all nodes in the graph
    print(visited)
    return visited == set(graph.keys())

# Example usage
graph = defaultdict(list)
graph['a'] = ['b', 'c']
graph['b'] = ['d', 'e']
graph['c'] = ['f']
graph['f'] = ['b']
graph['I'] = ['b']
graph['d'] = []
graph['e'] = []
graph['f'] = []

node = 'a'
if can_reach_all_nodes(graph, node):
    print(f"{node} can go to every other node in the graph")
else:
    print(f"{node} cannot go to every other node in the graph")
