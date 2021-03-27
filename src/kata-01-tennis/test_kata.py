import kata


def test_point():
    """Test that point defaults to an even match."""
    n = 1000
    avg = sum([kata.point() for _ in range(n)]) / n
    assert 0.45 < avg < 0.55


def test_point_with_weights():
    """Test that point appropriately accounts for weighting."""
    eps = 0.05
    n = 1000
    for i in range(10):
        weight = i / 10
        avg = sum([kata.point(weight=weight) for _ in range(n)]) / n
        assert weight - eps < avg < weight + eps
