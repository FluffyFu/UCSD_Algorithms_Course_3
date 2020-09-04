# Uses python3

from typing import List, Set
import sys


def acyclic(adj):
    graph = Graph(adj)
    has_cycle = graph.has_cycle()

    return 1 if has_cycle else 0


class Graph:
    """
    Object to store the graph and perform operation on the graph.
    """

    def __init__(self, adj: List[List[int]]):
        self._adj = adj
        self._on_stack = set()
        self._to_visit = {i for i in range(len(adj))}
        self._cycle = False

    def _has_cycle(self, x: int) -> None:
        """
        Internal function to test if there is a circle from node x.
        """
        self._on_stack.add(x)
        for v in self._adj[x]:
            if self._cycle:
                return
            elif v in self._to_visit:
                self._to_visit.remove(v)
                self._has_cycle(v)
            elif v in self._on_stack:
                self._cycle = True
        self._on_stack.remove(x)

    def has_cycle(self):
        """
        Check if the whole graph contains a circle.
        """
        while len(self._to_visit) > 0:
            if self._cycle:
                return True
            x = self._to_visit.pop()
            self._has_cycle(x)
        return False


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
