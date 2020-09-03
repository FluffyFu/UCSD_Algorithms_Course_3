# Uses python3

import sys
from typing import List
from queue import Queue


def reach_dfs(adj: List[int], x: int, y: int) -> int:
    """
    Check if node x and node y are connected in the given graph.
    """
    visited = [False for _ in range(len(adj))]
    visited[x] = True

    dfs(adj, visited, x)

    return 1 if visited[y] else 0


def reach_bfs(adj: List[int], x: int, y: int) -> int:
    visited = bfs(adj, x)
    return 1 if visited[y] else 0


def dfs(adj: List[int], visited: List[bool], start: int) -> None:
    """
    Perform depth-first search on the given graph with the given start node.
    """
    for v in adj[start]:
        if not visited[v]:
            visited[v] = True
            dfs(adj, visited, v)


def bfs(adj: List[int], start: int) -> List[bool]:
    """
    Perform breadth-first search on the given graph with the given start node and
    returns a list of bool that indicates if that node is visited.
    """
    visited = [False for _ in range(len(adj))]

    q = Queue()
    q.put(start)

    while not q.empty():
        v = q.get()
        for w in adj[v]:
            if not visited[w]:
                visited[w] = True
                q.put(w)
    return visited


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach_dfs(adj, x, y))
