# Uses python3
from typing import List, Set
import sys
sys.setrecursionlimit(200000)


class DirectedGraph:
    """
    An object used to store the directed graph and perform calculation on the number
    of SCC in the graph.
    """

    def __init__(self, adj: List[List[int]]):
        self._adj = adj
        self._reversed_graph = self._reverse_graph(adj)
        self._to_visit = {i for i in range(len(adj))}

    def _reverse_graph(self, adj: List[List[int]]) -> List[List[int]]:
        """
        Reverse the original graph.
        """
        reversed_graph = [[] for _ in range(len(adj))]

        for v in range(len(adj)):
            for w in adj[v]:
                reversed_graph[w].append(v)
        return reversed_graph

    def _dfs_post_order(self, x: int, post_order: List[int]) -> None:
        """
        Perform dfs on the reversed graph and collect the nodes in post order.
        """
        for v in self._reversed_graph[x]:
            if v in self._to_visit:
                self._to_visit.remove(v)
                self._dfs_post_order(v, post_order)
                post_order.append(v)
        post_order.append(x)

    def _dfs(self, x: int, visited: Set[int]) -> None:
        """
        Perform dfs on the graph with the given node.
        """
        for v in self._adj[x]:
            if not v in visited:
                visited.add(v)
                self._dfs(v, visited)

    def num_scc(self) -> int:
        """
        Computer the number of Strongly Connect Components by following steps:
            1. Calculate the reverse post order on the reversed graph.
            2. Perform dfs on the original graph with the reverse post order.
            3. Increase the counter for each dfs function call.
        """
        post_order = []

        while len(self._to_visit) > 0:
            x = self._to_visit.pop()
            self._dfs_post_order(x, post_order)

        reversed_post_order = post_order[::-1]
        count = 0
        visited = set()
        for v in reversed_post_order:
            if not v in visited:
                visited.add(v)
                self._dfs(v, visited)
                count += 1
        return count


def number_of_strongly_connected_components(adj):
    graph = DirectedGraph(adj)
    return graph.num_scc()


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
