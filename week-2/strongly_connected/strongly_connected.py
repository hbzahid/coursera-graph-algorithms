#Uses python3

import sys

sys.setrecursionlimit(200000)

def get_reversed_graph(adj):
    reversed_graph = [[] for _ in range(len(adj))]
    for v, neighbors in enumerate(adj):
        for neighbor in neighbors:
            reversed_graph[neighbor].append(v)
    return reversed_graph

# Returns a list of len(n) where list[i]
# is the vertex with postvisit number i
def compute_postvisit_numbers(adj):
    current = [0]
    visited = [False] * len(adj)
    postvisit_numbers = [0] * len(adj)

    def mark_postvisit_aux(v):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                mark_postvisit_aux(neighbor)
        postvisit_numbers[current[0]] = v
        current[0] += 1

    for v in range(len(adj)):
        if not visited[v]:
            mark_postvisit_aux(v)

    return postvisit_numbers

def number_of_strongly_connected_components(adj):
    result = 0
    visited = [False] * len(adj)
    reversed_graph = get_reversed_graph(adj)
    reversed_graph_postvisit_numbers = compute_postvisit_numbers(reversed_graph)

    def explore(v):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                explore(neighbor)

    for v in reversed(reversed_graph_postvisit_numbers):
        if not visited[v]:
            explore(v)
            result += 1

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
