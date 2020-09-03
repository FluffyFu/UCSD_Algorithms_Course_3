import pytest
from connected_components import number_of_components


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


def test_number_of_components(g1, g2):
    assert number_of_components(g1) == 1
    assert number_of_components(g2) == 2
