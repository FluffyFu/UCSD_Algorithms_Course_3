import pytest
from acyclicity import Graph


@pytest.fixture
def g1():
    adj = [None for _ in range(4)]
    adj[0] = [1]
    adj[1] = [2]
    adj[2] = [0]
    adj[3] = [0]

    return adj


@pytest.fixture
def g2():
    adj = [None for _ in range(5)]
    adj[0] = [1, 2, 3]
    adj[1] = [2, 4]
    adj[2] = [3, 4]
    adj[3] = []
    adj[4] = []

    return adj


def test_graph(g1, g2):
    graph1 = Graph(g1)
    assert graph1.has_cycle() == True

    graph2 = Graph(g2)
    assert graph2.has_cycle() == False
