import pytest
import kata01 as kata


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


@pytest.mark.parametrize(
    "scores, announcement",
    [
        ([0, 0], "Love All"),
        ([0, 1], "Love-Fifteen"),
        ([0, 2], "Love-Thirty"),
        ([0, 3], "Love-Forty"),
        ([1, 0], "Fifteen-Love"),
        ([1, 1], "Fifteen All"),
        ([1, 2], "Fifteen-Thirty"),
        ([1, 3], "Fifteen-Forty"),
        ([2, 0], "Thirty-Love"),
        ([2, 1], "Thirty-Fifteen"),
        ([2, 2], "Thirty All"),
        ([2, 3], "Thirty-Forty"),
        ([3, 0], "Forty-Love"),
        ([3, 1], "Forty-Fifteen"),
        ([3, 2], "Forty-Thirty"),
        ([3, 3], "Deuce"),
        ([4, 4], "Deuce"),
        ([5, 4], "Advantage Server"),
        ([6, 5], "Advantage Server"),
        ([4, 5], "Advantage Receiver"),
        ([5, 6], "Advantage Receiver"),
        ([4, 0], "Server Wins"),
        ([0, 4], "Receiver Wins"),
    ],
)
def test_announce(scores, announcement):
    """Test that the correct score is announced."""
    assert kata.announce(scores) == announcement


players = pytest.mark.parametrize(
    "weight, winner",
    [
        (0.0, 0),
        (1.0, 1),
    ],
)


@players
def test_game_winner_with_unfair_match(weight, winner):
    _winner, _ = kata.game(weight=weight)
    assert _winner == winner


@players
def test_game_set_winner_with_unfair_match(weight, winner):
    _winner, _ = kata.game_set(weight=weight)
    assert _winner == winner


@players
def test_game_match_winner_with_unfair_match(weight, winner):
    _winner, _ = kata.game_match(weight=weight)
    assert _winner == winner
