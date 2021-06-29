# Sözlükler ve setler gibi özyineleme ve veri yapıları kullanılarak kolaylıkla uygulanabilir.

# Using a Python dictionary to act as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = {None}  # Set to keep track of visited nodes.


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
dfs(visited, graph, 'A'.upper())
