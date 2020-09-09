# Uses python3

import sys
import queue
import numpy as np
from copy import deepcopy
from typing import List, Set


def bipartite(adj: List[List[int]]):
    graph = Graph(adj)
    return 1 if graph.is_bipartite() else 0


def bipartite_bfs(adj: List[List[int]]):
    graph = Graph(adj)
    return 1 if graph.is_bipartite_bfs() else 0


class Graph:
    """
    Determine if an undirected graph is bipartite.
    """

    def __init__(self, adj: List[List[int]]):
        self._adj = self._preprocess_adj(adj)
        self._colors = [False for i in range(len(adj))]
        self._visited = set()
        self._is_bipartite = True

    def _preprocess_adj(self, adj: List[List[int]]) -> List[Set[int]]:
        """
        Remove duplicate edges and self loop in the graph.
        """
        result = deepcopy(adj)
        for i in range(len(result)):
            result[i] = set(result[i])
            if i in result[i]:
                result[i].remove(i)

        return result

    def _dfs(self, s: int) -> None:
        self._visited.add(s)
        color = self._colors[s]
        for v in self._adj[s]:
            if not v in self._visited:
                self._colors[v] = (not color)
                self._dfs(v)
            elif self._colors[v] == color:
                self._is_bipartite = False

    def is_bipartite(self):
        for s in range(len(self._adj)):
            if not s in self._visited:
                self._dfs(s)

        return self._is_bipartite

    def is_bipartite_bfs(self) -> bool:
        """
        Test if a graph is bipartite with bfs.
        """
        colors = [False for _ in range(len(self._adj))]
        visited = set()
        q = queue.Queue()

        for i in range(len(self._adj)):
            # loop through CC.
            if not i in visited:
                q.put(i)
                while not q.empty():
                    s = q.get()
                    for v in self._adj[s]:
                        if not v in visited:
                            visited.add(v)
                            colors[v] = (not colors[s])
                            q.put(v)
                        elif colors[v] == colors[s]:
                            return False
        return True


def generate_random_graph(n_v: int, n_e: int, n_graphs=30) -> List[List[int]]:
    """
    Generate a random graph with the given number of vertices and
    edges. Return the graph in the form of an adjacent list.
    """
    adjs = []

    for _ in range(n_graphs):
        adj = [[] for _ in range(n_v)]

        for _ in range(n_e):
            v1, v2 = np.ranomd.randint(0, n_v, size=2)
            adj[v1].append(v2)
            adj[v2].append(v1)
        adjs.append(adj)

    return adjs


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
    print(bipartite(adj))
