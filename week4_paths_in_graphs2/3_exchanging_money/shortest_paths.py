# Uses python3

import sys
import queue
from typing import List, Tuple


def shortest_paths(adj, cost, s):
    sp = ShortestPath(adj, cost, s)
    return sp.reformat_results()


class ShortestPath:
    """
    Given a graph and a source, check each node in the graph to see which one of the
    followings it belongs to:

        1. not reachable from s.
        2. reachable from s but no shortest path (i.e. there exist a negative circle)
        3. reachable from s and there is no negative circle.

    The implementation steps are as follows:
        1. run Bellman-Ford and store all the vertices that has been relaxed on the V-th pass.
           These vertices does not have a shorted path from s. Note that this is not a complete
           list. We need to perform bfs to collect all of them.
        2. Those nodes still with inf distance are not reachable from s.
        3. The rest of vertices has shortest path from s and dst[s] stores the distance.
    """
    INFINITY = float('inf')

    def __init__(self, adj, cost, s):
        self._adj = adj
        self._cost = cost
        self._n_v = len(adj)
        self._not_reachable = None
        self._s = s

    def _dfs(self, s, visited):
        visited.add(s)
        for v in self._adj[s]:
            if not v in visited:
                self._dfs(v, visited)

    def _bellman_ford(self):
        dst = [self.INFINITY for _ in range(self._n_v)]
        dst[self._s] = 0

        for _ in range(self._n_v - 1):
            for v, neighbors in enumerate(self._adj):
                for i, w in enumerate(neighbors):
                    if dst[w] > dst[v] + self._cost[v][i]:
                        dst[w] = dst[v] + self._cost[v][i]
                        # node_to[w] = v

        no_sp_seed = set()

        # Find the nodes that are part of the negative cycle.
        # NOTE: this is no a complete list of cycle. Depending
        # on the edge relax order, some of the nodes in the negative
        # cycle may not get relaxed in one pass, it'll get relaxed in
        # the following pass though.
        for v, neighbors in enumerate(self._adj):
            for i, w in enumerate(neighbors):
                if dst[w] > dst[v] + self._cost[v][i]:
                    dst[w] = dst[v] + self._cost[v][i]
                    no_sp_seed.add(w)

        no_sp = set()
        q = queue.Queue()

        # Perform bfs to find all the nodes that does not have
        # a shortest path.
        while len(no_sp_seed) > 0:
            s = no_sp_seed.pop()
            if not s in no_sp:
                q.put(s)
                while not q.empty():
                    v = q.get()
                    no_sp.add(v)
                    for w in self._adj[v]:
                        if not w in no_sp:
                            q.put(w)

        return no_sp, dst

    def reformat_results(self):
        """
        Internal method to format the results for each node.
        If the node is not reachable from s, represent it with '*'.
        If the node has a path from s, but there's no shortest path, represent it with '-'.
        Otherwise, represent with the shortest distance.
        """
        np_sp, dst = self._bellman_ford()
        for i in np_sp:
            dst[i] = '-'

        for i in range(len(dst)):
            if dst[i] == float('inf'):
                dst[i] = '*'

        return dst


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
    s = data[0]
    s -= 1
    dist = shortest_paths(adj, cost, s)
    for x in range(n):
        print(dist[x])
