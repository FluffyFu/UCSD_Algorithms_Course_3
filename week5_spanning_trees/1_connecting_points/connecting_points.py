# Uses python3
import sys
import math
import queue


def minimum_distance(xs, ys):
    mst = LazyPrimMST(xs, ys)
    return mst.min_dist()


class LazyPrimMST:
    """
    Implement Prim's algorithm with a lazy approach (i.e. when the priority of a node
    changes, instead of modifying the priority in the PQ, we insert a new element to
    the PQ with the update priority.)

    The problem is:
    Given a list of 2D points, find the MST (the minimum distance sum).
    """

    def __init__(self, xs, ys):
        self._vertex = [(x, y) for x, y in zip(xs, ys)]
        self._n = len(xs)
        self._distance_matrix = self._cal_distance_matrix()

    def _cal_distance_matrix(self):
        res = [[None for _ in range(self._n)] for _ in range(self._n)]
        for i in range(self._n):
            for j in range(i, self._n):
                x_i, y_i = self._vertex[i]
                x_j, y_j = self._vertex[j]
                res[i][j] = math.sqrt((x_i - x_j)**2 + (y_i - y_j)**2)
        for i in range(self._n):
            for j in range(0, i):
                res[i][j] = res[j][i]

        return res

    def min_dist(self):
        visited = set()  # keep track of the nodes that are already in the MST
        # keep track of the nodes that haven't been visited yet.
        cost = 0
        pq = queue.PriorityQueue()
        # (dist, node_index), start from node-0
        pq.put((0, 0))

        while not pq.empty():
            weight, v = pq.get()
            if v in visited:
                continue
            visited.add(v)
            cost += weight
            for w in range(self._n):
                if not w in visited:
                    pq.put((self._distance_matrix[v][w], w))

        return cost


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
