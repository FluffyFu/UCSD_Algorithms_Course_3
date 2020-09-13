from shortest_paths import shortest_paths, generate_adj_cost
import pytest
import pudb


@pytest.fixture
def g1():
    n_v = 6
    edges = [
            [1, 2, 10],
            [2, 3, 5],
            [1, 3, 100],
            [3, 5, 7],
            [5, 4, 10],
            [4, 3, -18],
            [6, 1, -1]
    ]
    adj, cost = generate_adj_cost(n_v, edges)
    return adj, cost


@pytest.fixture
def g2():
    n_v = 5
    edges = [
            [1, 2, 1],
            [4, 1, 2],
            [2, 3, 2],
            [3, 1, -5]
    ]
    adj, cost = generate_adj_cost(n_v, edges)
    return adj, cost


@pytest.fixture
def g3():
    # Contains two negative cycles.
    n_v = 7
    edges = [
            [1, 2, 1],
            [2, 3, 1],
            [3, 4, 1],
            [4, 2, -3],
            [2, 5, 1],
            [5, 6, 1],
            [6, 7, 1],
            [7, 5, -3]
    ]
    adj, cost = generate_adj_cost(n_v, edges)
    return adj, cost


def test_shortest_paths_g1(g1):
    adj, cost = g1
    s = 0
    # pudb.set_trace()
    dst = shortest_paths(adj, cost, s)

    assert dst == [0, 10, '-', '-', '-', '*']


def test_shortest_paths_g2(g2):
    adj, cost = g2
    s = 3
    dst = shortest_paths(adj, cost, s)

    assert dst == ['-', '-', '-', 0, '*']


def test_shortest_paths_g3(g3):
    adj, cost = g3
    s = 0
    dst = shortest_paths(adj, cost, s)
    assert dst == [0, '-', '-', '-', '-', '-', '-']
