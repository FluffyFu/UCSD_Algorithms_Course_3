from reachability import reach_dfs, reach_bfs
import pytest


@pytest.fixture
def g1():
    adj = [None for _ in range(4)]
    adj[0] = [1, 3]
    adj[1] = [0, 2]
    adj[2] = [1]
    adj[3] = [2, 0]

    return adj


@pytest.fixture
def g2():
    adj = [None for _ in range(4)]
    adj[0] = [1]
    adj[1] = [0, 2]
    adj[2] = [1]
    adj[3] = []

    return adj


def test_reach_dfs(g1, g2):
    assert reach_dfs(g1, 0, 3) == 1
    assert reach_dfs(g2, 0, 3) == 0


def test_reach_bfs(g1, g2):
    assert reach_bfs(g1, 0, 3) == 1
    assert reach_bfs(g2, 0, 3) == 0

