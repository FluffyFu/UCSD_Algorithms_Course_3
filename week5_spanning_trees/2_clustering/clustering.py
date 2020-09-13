# Uses python3
import sys
import math
import queue


def clustering(xs, ys, k):
    mst = LazyPrimMST(xs, ys, k)
    return mst.distant()


class LazyPrimMST:
    """
    Implement Prim's algorithm with a lazy approach (i.e. when the priority of a node
    changes, instead of modifying the priority in the PQ, we insert a new element to
    the PQ with the update priority.)

    The problem is:
    Given a list of points and an integer k (k>=2), cluster the points into k groups.
    Find the largest d, where the distance between any two points in different clusters
    is at least d.

    Max(Min(dist(x_i, x_j))) where (i, j does not belong to the same cluster)

    We run Prim's algorithm in the standard way and store all the weights in the MST.
    The answer to this problem is the top(k-2) element in the weights.
    """

    def __init__(self, xs, ys, k):
        self._vertex = [(x, y) for x, y in zip(xs, ys)]
        self._n = len(xs)
        self._k = k
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

    def distant(self):
        visited = set()  # keep track of the nodes that are already in the MST
        # keep track of the nodes that haven't been visited yet.
        mst_weights = []
        pq = queue.PriorityQueue()
        # (dist, node_index), start from node-0
        pq.put((0, 0))

        while not pq.empty():
            weight, v = pq.get()
            if v in visited:
                continue
            visited.add(v)
            mst_weights.append(weight)
            for w in range(self._n):
                if not w in visited:
                    pq.put((self._distance_matrix[v][w], w))

        return sorted(mst_weights, reverse=True)[self._k-2]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
