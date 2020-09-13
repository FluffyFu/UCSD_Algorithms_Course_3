from connecting_points import minimum_distance
import pytest
import pudb


@pytest.fixture
def g1():
    xs = [0, 0, 1, 1]
    ys = [0, 1, 0, 1]
    return xs, ys


@pytest.fixture
def g2():
    xs = [0, 0, 1, 3, 3]
    ys = [0, 2, 1, 0, 2]
    return xs, ys


def test_minimum_distance_g1(g1):
    xs, ys = g1
    assert minimum_distance(xs, ys) == 3.0


def test_minimum_distance_g2(g2):
    xs, ys = g2
    assert minimum_distance(xs, ys) == pytest.approx(7.064495102)

