graph = {
    'a': ['b', 'c', 'e'],
    'b': ['d', 'f'],
    'c': ['g'],
    'e': ['f'],
    'f': ['e'],
}


def IDDFS(root, goal):
    depth = 0
    while True:
        print("Looping at depth %i " % (depth))
        result = DLS(root, goal, depth)
        print("Result: %s, Goal: %s" % (result, goal))
        if result == goal:
            return result
        depth = depth + 1


def DLS(node, goal, depth):
    print("node: %s, goal %s, depth: %i" % (node, goal, depth))
    if depth == 0 and node == goal:
        print(" --- Found goal, returning --- ")
        return node
    elif depth > 0:
        print("Looping through children: %s" % (graph.get(node, [])))
        for child in graph.get(node, []):
            if goal == DLS(child, goal, depth - 1):
                return goal


IDDFS('a', 'g')
