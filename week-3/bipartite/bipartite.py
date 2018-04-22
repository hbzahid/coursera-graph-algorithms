#Uses python3

import sys
import queue

RED = 1
BLUE = 2

def bipartite(adj):
    colors = [None] * len(adj)

    def is_bipartite(v):
        q = queue.Queue()
        q.put(v)
        colors[v] = RED
        while (not q.empty()):
            current = q.get()
            for neighbor in adj[current]:
                if colors[neighbor] is None:
                    q.put(neighbor)
                    colors[neighbor] = RED if colors[current] == BLUE else BLUE
                else:
                    if colors[neighbor] == colors[current]:
                        return False
        return True

    for v in range(len(adj)):
        if colors[v] is None:
            if not is_bipartite(v):
                return False
    return True

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
    print(int(bipartite(adj)))
