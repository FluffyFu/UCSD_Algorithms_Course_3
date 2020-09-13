from negative_cycle import negative_cycle, generate_adj_cost
import pytest
import pudb


@pytest.fixture
def g1():
    n_v = 4
    edges = [
            [1, 2, -5],
            [4, 1, 2],
            [2, 3, 2],
            [3, 1, 1]
    ]
    adj, cost = generate_adj_cost(n_v, edges)
    return adj, cost


@pytest.fixture
def g2():
    n_v = 10
    edges = [
            [1, 2, 1],
            [5, 6, 1],
            [6, 7, 1],
            [8, 9, 1],
            [9, 10, 1],
            [3, 4, 1],
            [7, 8, 1],
            [4, 5, 1],
            [2, 3, 1],
    ]
    adj, cost = generate_adj_cost(n_v, edges)
    return adj, cost


@pytest.fixture
def g3():
    n_v = 3
    edges = [
            [1, 2, 1],
            [2, 3, 1]
    ]
    adj, cost = generate_adj_cost(n_v, edges)
    return adj, cost


def test_negative_cycle_g1(g1):
    adj, cost = g1
    assert negative_cycle(adj, cost) == 1


def test_negative_cycle_g2(g2):
    adj, cost = g2
    assert negative_cycle(adj, cost) == 0


def test_negative_cycle_g3(g3):
    adj, cost = g3
    # pudb.set_trace()
    assert negative_cycle(adj, cost) == 0

