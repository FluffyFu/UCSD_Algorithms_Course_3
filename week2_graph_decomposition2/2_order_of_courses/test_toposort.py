import pytest
from toposort import Graph
import pudb


@pytest.fixture
def adj1():
    adj = [None for _ in range(4)]
    adj[0] = [1]
    adj[1] = []
    adj[2] = [0]
    adj[3] = [0]
    return adj


@pytest.fixture
def adj2():
    adj = [None for _ in range(4)]
    adj[0] = []
    adj[1] = []
    adj[2] = [0]
    adj[3] = []
    return adj


def test_graph(adj1, adj2):
    # pudb.set_trace()
    graph1 = Graph(adj1)
    order1 = graph1.topological_sort()
    assert (order1 == [3, 2, 0, 1]) or (order1 == [2, 3, 0, 1])

    graph2 = Graph(adj2)
    order2 = graph2.topological_sort()
    assert order2 == [3, 2, 1, 0]
