# Uses python3

import sys
from queue import PriorityQueue
from typing import List, Tuple


def distance(adj, cost, s, t):
    spt = ShortestPathTree(adj, cost)
    return spt.shortest_path_weight(s, t)


class ShortestPathTree:
    """
    Given a directed graph (possibly with cycles) with no negative weights. Find the shortest
    path cost from the given source and destination.

    Here we implement it using Dijkstra's algorithms with priority queue (lazy version, i.e. instead of
    changing the priority of an element in the queue, we add that element again to the PQ with a new weight.
    When pop out the min element from the PQ, we check if that node is already in the SPT.)
    """

    INFINITY = int(10E16)

    def __init__(self, adj: List[List[int]], cost: List[List[int]]) -> None:
        self._adj = adj
        self._cost = cost
        self._v = len(adj)

    def shortest_path_weight(self, s: int, t: int) -> int:
        """
        Return the minimum cost from source to target. If they are not connected, return -1.
        """
        dst = [self.INFINITY for _ in range(self._v)]
        spt = set()  # keep track of elements in the SPT
        pq = PriorityQueue()

        dst[s] = 0
        pq.put((dst[s], s))

        while (not pq.empty()) and (not t in spt):
            _, v = pq.get()
            if v in spt:
                # lazy pq, need to check the node is not in SPT
                continue
            else:
                for i, w in enumerate(self._adj[v]):
                    if w in spt:
                        # only need to relax nodes that are not in SPT
                        continue
                    if dst[w] > dst[v] + self._cost[v][i]:
                        dst[w] = dst[v] + self._cost[v][i]
                        pq.put((dst[w], w))
                spt.add(v)
                # add v to SPT when all its neighbors have been relaxed.

        return dst[v] if t in spt else -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
