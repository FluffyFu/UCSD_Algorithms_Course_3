import pytest
import numpy as np
import pudb
from hypothesis import given, assume, strategies as st
from bipartite import bipartite, bipartite_bfs, generate_random_graph


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
    adj[0] = [3]
    adj[1] = [3, 4]
    adj[2] = [3]
    adj[3] = [0, 1]
    adj[4] = [1]

    return adj


@pytest.fixture
def adj3():
    adj = [None for _ in range(5)]
    adj[0] = [1, 3]
    adj[1] = [0, 2]
    adj[2] = [1, 3, 4]
    adj[3] = [0, 2, 4]
    adj[4] = [2, 3]

    return adj


@pytest.fixture
def adj4():
    adj = [None for _ in range(7)]
    adj[0] = [1]
    adj[1] = [0, 2, 6]
    adj[2] = [1, 3, 5]
    adj[3] = [2, 4]
    adj[4] = [3, 5]
    adj[5] = [2, 4, 6]
    adj[6] = [1, 5]

    return adj


@pytest.fixture
def adj5():
    adj = [None for _ in range(5)]
    adj[0] = [3, 4]
    adj[1] = [3, 4]
    adj[2] = [4]
    adj[3] = [0, 1]
    adj[4] = [0, 1]

    return adj


@pytest.fixture
def adj6():
    # same as adj6 but with repeated edges between nodes.
    adj = [None for _ in range(5)]
    adj[0] = [0, 3, 3, 3, 4]
    adj[1] = [3, 3, 4]
    adj[2] = [4]
    adj[3] = [1, 1, 0, 0, 0]
    adj[4] = [0, 1, 2]

    return adj


def test_bipartite(adj1, adj2, adj3, adj4, adj5, adj6):
    assert bipartite(adj1) == 0
    # pudb.set_trace()
    assert bipartite(adj2) == 1
    assert bipartite(adj3) == 0
    assert bipartite(adj4) == 1
    assert bipartite(adj5) == 1
    assert bipartite(adj6) == 1


def test_bipartite_bfs(adj1, adj2, adj3, adj4, adj5, adj6):
    # pudb.set_trace()
    assert bipartite_bfs(adj1) == 0
    assert bipartite_bfs(adj2) == 1
    assert bipartite_bfs(adj3) == 0
    assert bipartite_bfs(adj4) == 1
    assert bipartite_bfs(adj5) == 1
    assert bipartite_bfs(adj6) == 1


@given(st.integers(min_value=1, max_value=1000), st.integers(min_value=1, max_value=50000))
def stress_test(n_v, n_e):
    adjs = generate_random_graph(n_v, n_e, n_graphs=100)

    for adj in adjs:
        assert bipartite(adj) == bipartite_bfs(adj)
