import pytest
from strongly_connected import DirectedGraph
import pudb


@pytest.fixture
def adj1():
    adj = [None for _ in range(4)]
    adj[0] = [1]
    adj[1] = [2]
    adj[2] = [0]
    adj[3] = [0]

    return adj


@pytest.fixture
def adj2():
    adj = [None for _ in range(5)]
    adj[0] = []
    adj[1] = [0]
    adj[2] = [0, 1]
    adj[3] = [0, 2]
    adj[4] = [1, 2]
    return adj


@pytest.fixture
def adj3():
    adj = [None for _ in range(4)]
    adj[0] = [1]
    adj[1] = []
    adj[2] = [1]
    adj[3] = [2]

    return adj


def test_directed_graph(adj1, adj2, adj3):
    # pudb.set_trace()
    g1 = DirectedGraph(adj1)
    assert g1.num_scc() == 2

    g2 = DirectedGraph(adj2)
    assert g2.num_scc() == 5

    g3 = DirectedGraph(adj3)
    assert g3.num_scc() == 4
