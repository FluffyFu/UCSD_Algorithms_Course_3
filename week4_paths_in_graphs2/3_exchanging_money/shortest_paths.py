# Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # write your code here
    pass


class ShortestPath:
    """
    Given a graph and a source, check each node in the graph to see which one of the
    followings it belongs to:

        1. not reachable from s.
        2. reachable from s but no shortest path (i.e. there exist a negative circle)
        3. reachable from s and there is no negative circle.

    The implementation steps are as follows:
        1. run dfs from s and find out those that are not reachable from s.
        2. run Bellman-Ford and store all the vertices that has been relaxed on the V-th pass.
           These vertices does not have a shorted path from s.
        3. The rest of vertices has shortest path from s and dst[s] stores the distance.
    """
    INFINITY = int(10E16)

    def __init__(self, adj, cost, s):
        self._adj = adj
        self._cost = cost
        self._n_v = len(adj)
        self._not_reachable = None
        self._s = s

    @property
    def not_reachable(self):
        if self._not_reachable != None:
            return self._not_reachable
        else:
            self._not_reachable = self._generate_not_reachable()
            return self._not_reachable

    def _generate_not_reachable(self):
        """
        Internal method to generate a set of vertices this not reachable from the source.
        """
        visited = set()
        self._dfs(self._s, visited)

        return {i for i in range(self._n_v)} - visited

    def _dfs(self, s, visited):
        visited.add(s)
        for v in self._adj[s]:
            if not v in visited:
                self._dfs(s, visited)

    def _bellman_ford(self):
        dst = [self.INFINITY for _ in range(self._n_v)]
        dst[self._s] = 0

        for _ in range(self._n_v - 1):
            for v, neighbors in enumerate(self._adj):
                for i, w in enumerate(neighbors):
                    if dst[w] > dst[v] + self._cost[v][i]:
                        dst[w] = dst[v] + self._cost[v][i]

        no_sp = set()

        for v, neighbors in enumerate(self._adj):
            for i, w in enumerate(neighbors):
                if dst[w] > dst[v] + self._cost[v][i]:
                    no_sp.add(w)

        return no_sp, dst


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
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

