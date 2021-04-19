import kata04 as kata
import pytest


@pytest.mark.parametrize(
    "n, discount",
    [
        (1, 1.00),
        (2, 0.95),
        (3, 0.90),
        (4, 0.80),
        (5, 0.75),
    ],
)
def test_no_duplicates(n, discount):
    order = [1] * n
    assert kata.order_total(order) == (8 * n * discount)


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
def test_all_duplicates(n):
    order = [n]
    assert kata.order_total(order) == (8 * n)


def test_mix():
    order = [2, 2, 2, 1, 1]
    price = 8 * ((5 * 0.75) + (3 * 0.90))
    assert kata.order_total(order) == price
