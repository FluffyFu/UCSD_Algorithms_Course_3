import pytest
import pudb
from clustering import clustering


@pytest.fixture
def g1():
    xs = [7, 4, 5, 1,
          2, 5, 3, 7,
          2, 4, 6, 2]
    ys = [6, 2, 1, 7,
          7, 7, 3, 8,
          8, 4, 7, 6]
    k = 3

    return xs, ys, k


@pytest.fixture
def g2():
    xs = [3, 1, 4, 9,
          9, 8, 3, 4]
    ys = [1, 2, 6, 8,
          9, 9, 11, 12]
    k = 4

    return xs, ys, k


def test_clustering_g1(g1):
    assert clustering(*g1) == pytest.approx(2.828427124746)


def test_clustering_g2(g2):
    assert clustering(*g2) == pytest.approx(5.0)
