from dijkstra import distance, generate_adj_cost
import pytest
import pudb


@pytest.fixture
def g1():
    n_e = 4
    edges = [
            [1, 2, 1],
            [4, 1, 2],
            [2, 3, 2],
            [1, 3, 5]
    ]
    return n_e, edges


@pytest.fixture
def g2():
    n_e = 5
    edges = [
            [1, 2, 4],
            [1, 3, 2],
            [2, 3, 2],
            [3, 2, 1],
            [2, 4, 2],
            [3, 5, 4],
            [5, 4, 1],
            [2, 5, 3],
            [3, 4, 4]
    ]
    return n_e, edges


@pytest.fixture
def g3():
    n_e = 3
    edges = [
            [1, 2, 7],
            [1, 3, 5],
            [2, 3, 2]
    ]
    return n_e, edges


def test_distance_g1(g1):
    n_e, edges = g1
    adj, cost = generate_adj_cost(n_e, edges)
    s, t = 0, 2

    # pudb.set_trace()
    assert distance(adj, cost, s, t) == 3


def test_distance_g2(g2):
    n_e, edges = g2
    adj, cost = generate_adj_cost(n_e, edges)
    s, t = 0, 4

    assert distance(adj, cost, s, t) == 6


def test_distance_g3(g3):
    n_e, edges = g3
    adj, cost = generate_adj_cost(n_e, edges)
    s, t = 2, 1

    assert distance(adj, cost, s, t) == -1

