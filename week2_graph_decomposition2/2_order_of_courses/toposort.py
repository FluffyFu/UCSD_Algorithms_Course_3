# Uses python3

import sys
from typing import List, Set


def toposort(adj):
    graph = Graph(adj)
    return graph.topological_sort()


class Graph:
    """
    Object used to perform topological sort on the given graph. The given
    graph is supposed to be a DAG.
    """

    def __init__(self, adj: List[List[int]]):
        self._adj = adj
        self._to_visit = {i for i in range(len(adj))}

    def _dfs(self, x: int, stack) -> None:
        """
        Internal function to perform dfs from the given node.
        """
        for v in self._adj[x]:
            if v in self._to_visit:
                self._to_visit.remove(v)
                self._dfs(v, stack)
        stack.append(x)

    def topological_sort(self) -> List[int]:
        """
        Return one topological order of the graph.
        """
        stack = []

        while len(self._to_visit) > 0:
            x = self._to_visit.pop()
            self._dfs(x, stack)

        return stack[::-1]


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
