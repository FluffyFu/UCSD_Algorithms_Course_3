# Uses python3

import sys
from typing import List, Tuple


def negative_cycle(adj, cost):
    nc = NegativeCycle(adj, cost)
    return nc.has_negative_cycle()


class NegativeCycle:
    """
    Check if a graph contains any negative cycle with Bellman-Ford algorithms.
    """
    INFINITY = int(1E16)

    def __init__(self, adj, cost):
        self._adj = adj
        self._cost = cost
        self._n_v = len(adj)
        self._dst = [self.INFINITY for _ in range(self._n_v)]

    def has_negative_cycle(self):
        """
        Assume all the vertices
        """
        # go through v-1 passes
        for _ in range(self._n_v - 1):
            # relax all the edges
            for v, neighbors in enumerate(self._adj):
                for i, w in enumerate(neighbors):
                    if self._dst[w] > self._dst[v] + self._cost[v][i]:
                        self._dst[w] = self._dst[v] + self._cost[v][i]

        # perform v+1 pass, if there is still vertices to relax, there
        # exist a negative cycle.
        for v, neighbors in enumerate(self._adj):
            for i, w in enumerate(neighbors):
                if self._dst[w] > self._dst[v] + self._cost[v][i]:
                    return 1
        return 0


def generate_adj_cost(n_v: int, edges: List[List[int]]) -> Tuple[List[List[int]], List[List[int]]]:
    adj = [[] for _ in range(n_v)]
    cost = [[] for _ in range(n_v)]

    for a, b, w in edges:
        adj[a-1].append(b-1)
        cost[a-1].append(w)

    return adj, cost


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
