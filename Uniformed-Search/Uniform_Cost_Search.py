import queue as Q


def search(graph, start, end):


    queue = Q.PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]

        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break

        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))


def readGraph():
    lines = int(input())
    graph = {}

    for line in range(lines):
        line = input()

        tokens = line.split()
        node = tokens[0]
        graph[node] = {}

        for i in range(1, len(tokens) - 1, 2):
            graph[node][tokens[i]] = int(tokens[i + 1])

    return graph


def main():
    graph = {'Balikesir': {'Istanbul': 155}, 'Canakkale': {'Istanbul': 125}, 'Izmir': {'Mugla': 190}, 'Istanbul': {'Samsun': 215}, 'Eskisehir': {'Konya': 120}, 'Ankara': {'Samsun': 115}, 'Mugla': {'Antalya': 80}, 'Antalya': {'Adana': 80}, 'Samsun': {'Trabzon': 120}, 'Kayseri': {'Adana': 245}, 'Trabzon': {'Rize': 75}, 'Rize': {'Diyarbakir': 165}}


    search(graph, 'Istanbul', 'Kayseri')


if __name__ == "__main__":
    main()
