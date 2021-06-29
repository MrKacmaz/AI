# Use dictionary

# 1-)   Herhangi bir düğümü seçin, bitişikteki ziyaret edilmemiş köşeyi ziyaret edin,
# ziyaret edildi olarak işaretleyin, görüntüleyin ve bir sıraya ekleyin.

# 2-)   Kalan bitişik tepe noktası yoksa, ilk tepe noktasını kuyruktan çıkarın

# 3-)   Sıra boşalana veya istenen düğüm bulunana kadar 1. ve 2. adımları tekrarlayın.

# Time Complexity
# Since all of the nodes and vertices are visited, the time complexity for BFS on a graph is O(V + E);
# where V is the number of vertices and E is the number of edges.

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfs(node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
bfs("d".upper())
