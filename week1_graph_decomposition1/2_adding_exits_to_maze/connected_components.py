# Uses python3

import sys
from typing import List, Set


def number_of_components(adj: List[List[int]]) -> int:
    """
    Calculate the number of connected components.
    """
    n_cc = 0
    unvisited = {i for i in range(len(adj))}

    while len(unvisited) > 0:
        v = unvisited.pop()
        dfs(adj, unvisited, v)
        n_cc += 1

    return n_cc


def dfs(adj: List[List[int]], unvisited: Set[int], start: int) -> None:
    """
    Internal function to perform dfs search on the graph.
    """
    for v in adj[start]:
        if v in unvisited:
            unvisited.remove(v)
            dfs(adj, unvisited, v)


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
    print(number_of_components(adj))
