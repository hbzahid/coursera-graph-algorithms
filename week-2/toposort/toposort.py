#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    pass

def toposort(adj):
    postvisit_number = [0]
    visited = [False] * len(adj)
    postvisit_numbers = [0] * len(adj)

    def explore(v):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                explore(neighbor)
        postvisit_numbers[postvisit_number[0]] = v
        postvisit_number[0] += 1

    for v in range(len(adj)):
        if not visited[v]:
            explore(v)

    order = postvisit_numbers[::-1]
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

