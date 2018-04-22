#Uses python3

import sys
import queue
import math
from collections import deque

def distance(adj, s, t):
    distances = [-1] * len(adj)

    def run_bfs():
        queue = deque([])
        queue.append(s)
        distances[s] = 0
        while (len(queue) > 0):
            current = queue.popleft()
            for neighbor in adj[current]:
                if distances[neighbor] == -1:
                    queue.append(neighbor)
                    distances[neighbor] = distances[current] + 1
                    if neighbor == t:
                        return

    run_bfs()
    return distances[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
