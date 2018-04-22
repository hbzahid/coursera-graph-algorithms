#Uses python3

import sys


def acyclic(adj):
    visited = [False] * len(adj)
    rec_stack = [False] * len(adj)

    def has_cycle(v):
        if not visited[v]:
            visited[v] = True
            rec_stack[v] = True

            for neighbor in adj[v]:
                if (not visited[neighbor] and has_cycle(neighbor)) or rec_stack[neighbor]:
                    return True
        rec_stack[v] = False
        return False

    for v, neighbors in enumerate(adj):
        if has_cycle(v):
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
