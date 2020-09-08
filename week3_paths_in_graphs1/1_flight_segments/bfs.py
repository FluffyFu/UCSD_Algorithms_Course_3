# Uses python3

import sys
import queue


def distance(adj, s, t):
    graph = Graph(adj)

    return graph.bfs(s, t)


class Graph:

    def __init__(self, adj):
        self._adj = adj

    def bfs(self, s: int, t: int) -> int:
        """
        Perform bfs on the graph from node s. If t is reachable from s, return
        the distance. Otherwise, returns -1.

        Maintain a distances list, which contains the distance from the origin to
        a given node. It also plays the role memorizing which node has been visited.
        """

        q = queue.Queue()
        q.put(s)
        distances = [-1 for _ in range(len(self._adj))]
        distances[s] = 0

        while not q.empty():
            v = q.get()
            for w in self._adj[v]:
                if distances[w] == -1:
                    q.put(w)
                    distances[w] = distances[v] + 1

        return distances[t]


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
