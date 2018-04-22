#Uses python3

import sys
import heapq
import random
import math

class Vertex(object):
    def __init__(self, id, priority):
        self.id = id
        self.priority = priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.id == other.id
        else:
            return False

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return str((self.id, self.priority))

    def __repr__(self):
        return str((self.id, self.priority))

    def set_priority(self, priority):
        self.priority = priority

class DijkstraMinHeap(object):
    def __init__(self):
        self.data = []
        self.position_map = {}

    def bubble_up(self, position):
        parent = (position - 1) // 2
        while (parent >= 0 and self.data[parent] > self.data[position]):
            current_node = self.data[position]
            parent_node = self.data[parent]
            self.position_map[current_node] = parent
            self.position_map[parent_node] = position
            self.data[parent] = current_node
            self.data[position] = parent_node
            position = parent
            parent = (position - 1) // 2

    def bubble_down(self, position):
        swapped = True
        current = position
        while swapped:
            swapped = False
            smallest = current
            left = 2 * current + 1
            right = 2 * current + 2
            if left < self.size() and self.data[left] < self.data[smallest]:
                smallest = left
            if right < self.size() and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest != current:
                swapped = True
                smallest_node = self.data[smallest]
                current_node = self.data[current]
                self.position_map[smallest_node] = current
                self.position_map[current_node] = smallest
                self.data[smallest] = current_node
                self.data[current] = smallest_node
                current = smallest

    def push(self, vertex):
        self.position_map[vertex] = len(self.data)
        self.data.append(vertex)
        self.bubble_up(self.position_map[vertex])

    def pop(self):
        if self.size() == 1:
            return self.data.pop()
        last = self.data[-1]
        self.position_map[last] = 0
        self.data[-1], self.data[0] = self.data[0], self.data[-1]
        min_elt = self.data.pop()
        del self.position_map[min_elt]
        self.bubble_down(0)
        return min_elt

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

    def decrease_key(self, changed_vertex):
        position = self.position_map[changed_vertex]
        self.bubble_up(position)

def distance(adj, weights, s, t):
    dist = []
    heap = DijkstraMinHeap()
    for v in range(len(adj)):
        if v == s:
            d = 0
        else:
            d = float("inf")
        vertex = Vertex(v, d)
        heap.push(vertex)
        dist.append(vertex)

    while not heap.empty():
        v = heap.pop()
        for neighbor, cost in zip(adj[v.id], weights[v.id]):
            neighbor_vertex = dist[neighbor]
            new_distance = dist[v.id].priority + cost
            if dist[neighbor].priority > new_distance:
                neighbor_vertex.set_priority(new_distance)
                heap.decrease_key(neighbor_vertex)

    if dist[t].priority == float("inf"):
        return -1
    else:
        return dist[t].priority

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
