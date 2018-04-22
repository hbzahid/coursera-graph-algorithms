#Uses python3
import sys
import math
from collections import namedtuple

POINT = namedtuple('Point', ['x', 'y'])

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

class MinHeap(object):
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

    def __contains__(self, vertex):
        return vertex in self.position_map

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

    def decrease_key(self, changed_vertex):
        position = self.position_map[changed_vertex]
        self.bubble_up(position)

def minimum_distance(x, y):
    def get_points_from_coords(xcoords, ycoords):
        points = []
        for x, y in zip(xcoords, ycoords):
            points.append(POINT(x, y))
        return points

    def compute_weights(points):
        distances = [[] for _ in range(len(points))]
        for i, p1 in enumerate(points):
            for p2 in points:
                dist = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
                distances[i].append(dist)
        return distances

    #assume that each vertex is connected to every other vertex
    reference_vertex = 0
    min_spanning_distance = 0
    prev = None
    points = get_points_from_coords(x, y)
    weights = compute_weights(points)

    heap = MinHeap()
    distances = []
    for v in range(len(points)):
        if v == reference_vertex:
            d = 0
        else:
            d = float("inf")
        vertex = Vertex(v, d)
        heap.push(vertex)
        distances.append(vertex)

    while not heap.empty():
        v = heap.pop()
        if prev is not None:
            min_spanning_distance += distances[v.id].priority
        prev = v
        for neighbor, cost in enumerate(weights[v.id]):
            neighbor_vertex = distances[neighbor]
            if neighbor_vertex in heap and \
                neighbor_vertex.priority > cost:
                neighbor_vertex.set_priority(cost)
                heap.decrease_key(neighbor_vertex)

    return min_spanning_distance


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    minimum_distance(x, y)
    print("{0:.9f}".format(minimum_distance(x, y)))
