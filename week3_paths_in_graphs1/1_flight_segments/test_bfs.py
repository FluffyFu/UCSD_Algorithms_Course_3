import pytest
import pudb
from bfs import Graph, distance


@pytest.fixture
def adj1():
    adj = [None for _ in range(4)]
    adj[0] = [1, 3]
    adj[1] = [0, 2]
    adj[2] = [0, 1]
    adj[3] = [0]

    return adj


@pytest.fixture
def adj2():
    adj = [None for _ in range(5)]
    adj[0] = [2, 3]
    adj[1] = [4]
    adj[2] = [0, 3]
    adj[3] = [0, 2]
    adj[4] = [1]

    return adj


@pytest.fixture
def adj3():
    adj = [None for _ in range(3)]
    adj[0] = [1, 2]
    adj[1] = [0, 2]
    adj[2] = [1, 2]

    return adj


def test_distance(adj1, adj2, adj3):
    assert distance(adj1, 1, 3) == 2
    assert distance(adj2, 2, 4) == -1
    assert distance(adj3, 0, 1) == 1
    # pudb.set_trace()
    assert distance(adj3, 0, 2) == 1
