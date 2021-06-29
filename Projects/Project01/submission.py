"""
@author Alperen KACMAZ

"""

import csv
import heapq
from queue import PriorityQueue


class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0


class Node:

    def __init__(self, key):
        # self.key is the key of node
        # self.successors are the successors nodes
        # self.weight_successors represents weight of edges
        self.key, self.successors, self.weight_successors = key, [], {}

    # return the key
    def getKey(self):
        return self.key

    # return the successors of node
    def getSuccessors(self):
        return self.successors

    # add a node successor passing the node and the weight
    def addSuccessor(self, node, weight):
        # adds if successor node not exists
        if node.getKey() not in self.weight_successors:
            self.successors.append(node)
            self.weight_successors[node.getKey()] = weight

    # returns weight of successors
    def getWeightSuccessors(self):
        return self.weight_successors


# class that represents a graph
class Graph:

    def __init__(self):
        self.nodes = {}  # key: key of node, value: instance of Node

    # adds a node in the graph passing a key
    def addNode(self, key_node):
        if key_node in self.nodes:  # checks if the key already exists
            print('Error: key %s already exists!!' % key_node)
        else:
            node = Node(key_node)  # creates a instance of Node
            self.nodes[key_node] = node  # stores the node

    # connects the nodes
    def connect(self, key_source, key_destination, weight):
        # checks if the keys exists in the graph
        if key_source in self.nodes and key_destination in self.nodes:
            if key_source != key_destination:  # checks if the keys are differences
                if weight > 0:  # checks if the weight is positive
                    # connects the nodes
                    self.nodes[key_source].addSuccessor(self.nodes[key_destination], weight)
                else:
                    print('Error: weight negative!!')
            else:
                print('Error: same keys!!')
        else:
            print('Error: key not exists!!')

    # returns weight of edge
    def getWeightEdge(self, key_source, key_successor):
        if key_source in self.nodes and key_successor in self.nodes:  # checks if the keys exists
            if key_source != key_successor:  # checks if the keys are differences
                weight_successors = self.nodes[key_source].getWeightSuccessors()
                if key_successor in weight_successors:  # checks if key_successor is a successor
                    return weight_successors[key_successor]  # returns the weight
                else:
                    print('Error: successor not exists!!')
            else:
                print('Error: same keys!!')
        else:
            print('Error: key not exists!!')

    # returns the keys of all successors of a node
    def getSuccessors(self, key_node):
        if key_node in self.nodes:
            nodes = self.nodes[key_node].getSuccessors()
            keys_successors = [node.getKey() for node in nodes]
            return keys_successors
        else:
            print('Error: key not exists!!')

    # returns all nodes
    def getNodes(self):
        return self.nodes


# Implement this function to perform uniform cost search on the graph.
def uniform_cost_search(graph, key_node_start, key_node_goal, verbose=False):
    # UCS uses priority queue, priority is the cumulative cost (smaller cost)
    queue = PriorityQueue()

    # expands initial node

    # get the keys of all successors of initial node
    keys_successors = graph.getSuccessors(key_node_start)

    # adds the keys of successors in priority queue
    for key_sucessor in keys_successors:
        weight = graph.getWeightEdge(key_node_start, key_sucessor)
        # each item of queue is a tuple (key, cumulative_cost)
        queue.insert((key_sucessor, weight), weight)

    reached_goal, cumulative_cost_goal = False, -1
    while not queue.is_empty():
        # remove item of queue, remember: item of queue is a tuple (key, cumulative_cost)
        key_current_node, cost_node = queue.remove()
        if key_current_node == key_node_goal:
            reached_goal, cumulative_cost_goal = True, cost_node
            break

        if verbose:
            # shows a friendly message
            print('Node \'%s\' with cost %s ...' % (key_current_node, cost_node))

        # get all successors of key_current_node
        keys_successors = graph.getSuccessors(key_current_node)

        if keys_successors:  # checks if contains successors
            # insert all successors of key_current_node in the queue
            for key_sucessor in keys_successors:
                cumulative_cost = graph.getWeightEdge(key_current_node, key_sucessor) + cost_node
                queue.insert((key_sucessor, cumulative_cost), cumulative_cost)

    if reached_goal:
        print('\nReached goal! Cost: %s\n' % cumulative_cost_goal)
    else:
        print('\nUnfulfilled goal.\n')


def fileRead():
    destination = "data\\cities.csv"
    try:
        lines, cityFrom, cityTo, Depth = 0, [], [], []
        with open(destination, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                lines += 1
                cityFrom.append(row[0])
                cityTo.append(row[1])
                Depth.append(row[2])
        cityFrom.pop(0)
        cityTo.pop(0)
        Depth.pop(0)
        uniqueCities = set(cityFrom + cityTo)
        return cityFrom, cityTo, Depth, (lines - 1), uniqueCities
    except FileNotFoundError as f_error:
        print(f_error)


if __name__ == "__main__":
    # build the graph...
    # adds nodes in the graph
    startCity = str(input("Start location: ")).capitalize()
    goalCity = str(input("Finish location: ")).capitalize()
    city1, city2, depth, line, uniqueCities = fileRead()

    try:
        if startCity not in uniqueCities or goalCity not in uniqueCities:
            raise CityNotFoundError('\'%s\' or \'%s\'' % (startCity, goalCity))
        else:
            newGraph = Graph()
            for i in uniqueCities:
                newGraph.addNode(i)

            for i in range(line):
                newGraph.connect(city1[i], city2[i], int(depth[i]))

            for i in range(line):
                newGraph.connect(city2[i], city1[i], int(depth[i]))
            uniform_cost_search(graph=newGraph, key_node_start=startCity, key_node_goal=goalCity, verbose=True)

    except CityNotFoundError as e_city:
        print()
