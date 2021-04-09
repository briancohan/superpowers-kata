import kata02 as kata
import pytest


@pytest.mark.parametrize("n_dice", [0, 1, 2, 3, 4, 6, 7])
def test_wrong_number_of_dice(n_dice):
    dice = kata.roll(n_dice)
    with pytest.raises(kata.InvalidRoll) as exc_info:
        kata.score_chance(dice)
    assert "You must roll 5 dice" in exc_info.value.args[0]
    assert exc_info.type is kata.InvalidRoll
    assert issubclass(exc_info.type, kata.KataError)


@pytest.mark.parametrize("wrong", [0, 7, "a"])
def test_invalid_dice(wrong):
    dice = [1, 2, 3, 4, wrong]
    with pytest.raises(kata.InvalidDie) as exc_info:
        kata.score_chance(dice)
    assert "invalid die" in exc_info.value.args[0]
    assert exc_info.type is kata.InvalidDie
    assert issubclass(exc_info.type, kata.KataError)


def test_valid_roll_works_with_args_or_kwargs():
    with pytest.raises(kata.InvalidRoll) as exc_info:
        kata.score_chance()
    with pytest.raises(kata.InvalidRoll) as exc_info:
        kata.score_chance([1])
    with pytest.raises(kata.InvalidRoll) as exc_info:
        kata.score_chance(dice=[1, 1, 1, 1])


@pytest.mark.parametrize("dice", [(6,), (6, 6, 6)])
def test_valid_roll_with_2_d6(dice):
    @kata.valid_roll(n_dice=2)
    def func(*args, **kwargs):
        pass

    with pytest.raises(kata.InvalidRoll) as exc_info:
        func(dice=dice)


def test_valid_roll_with_5_d4():
    @kata.valid_roll(sides=4)
    def func(*args, **kwargs):
        pass

    with pytest.raises(kata.InvalidDie) as exc_info:
        func(dice=[2, 3, 4, 5, 6])


@pytest.mark.parametrize("n_dice", [1, 2, 3, 4, 5])
def test_roll_d6(n_dice):
    roll = kata.roll(n_dice)
    assert len(roll) == n_dice
    assert min(roll) >= 1
    assert max(roll) <= 6


@pytest.mark.parametrize(
    "dice, score",
    [
        ([6, 6, 6, 6, 6], 0),
        ([1, 6, 6, 6, 6], 1),
        ([1, 1, 6, 6, 6], 2),
        ([1, 1, 1, 6, 6], 3),
        ([1, 1, 1, 1, 6], 4),
        ([1, 1, 1, 1, 1], 5),
    ],
)
def test_score_ones(dice, score):
    assert kata.score_ones(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([6, 6, 6, 6, 6], 0),
        ([2, 6, 6, 6, 6], 2),
        ([2, 2, 6, 6, 6], 4),
        ([2, 2, 2, 6, 6], 6),
        ([2, 2, 2, 2, 6], 8),
        ([2, 2, 2, 2, 2], 10),
    ],
)
def test_score_twos(dice, score):
    assert kata.score_twos(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([6, 6, 6, 6, 6], 0),
        ([3, 6, 6, 6, 6], 3),
        ([3, 3, 6, 6, 6], 6),
        ([3, 3, 3, 6, 6], 9),
        ([3, 3, 3, 3, 6], 12),
        ([3, 3, 3, 3, 3], 15),
    ],
)
def test_score_threes(dice, score):
    assert kata.score_threes(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([6, 6, 6, 6, 6], 0),
        ([4, 6, 6, 6, 6], 4),
        ([4, 4, 6, 6, 6], 8),
        ([4, 4, 4, 6, 6], 12),
        ([4, 4, 4, 4, 6], 16),
        ([4, 4, 4, 4, 4], 20),
    ],
)
def test_score_fours(dice, score):
    assert kata.score_fours(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([6, 6, 6, 6, 6], 0),
        ([5, 6, 6, 6, 6], 5),
        ([5, 5, 6, 6, 6], 10),
        ([5, 5, 5, 6, 6], 15),
        ([5, 5, 5, 5, 6], 20),
        ([5, 5, 5, 5, 5], 25),
    ],
)
def test_score_fives(dice, score):
    assert kata.score_fives(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([1, 1, 1, 1, 1], 0),
        ([1, 1, 1, 1, 6], 6),
        ([1, 1, 1, 6, 6], 12),
        ([1, 1, 6, 6, 6], 18),
        ([1, 6, 6, 6, 6], 24),
        ([6, 6, 6, 6, 6], 30),
    ],
)
def test_score_sixes(dice, score):
    assert kata.score_sixes(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([1, 1, 1, 1, 1], 5),
        ([1, 1, 1, 1, 2], 6),
        ([1, 1, 1, 2, 2], 7),
        ([1, 1, 2, 2, 3], 0),
    ],
)
def test_3_of_kind(dice, score):
    assert kata.score_3_of_kind(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([1, 1, 1, 1, 1], 5),
        ([1, 1, 1, 1, 2], 6),
        ([1, 1, 1, 2, 2], 0),
    ],
)
def test_4_of_kind(dice, score):
    assert kata.score_4_of_kind(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([1, 1, 1, 1, 1], 0),
        ([1, 1, 2, 3, 3], 0),
        ([1, 1, 1, 2, 2], 25),
        ([1, 1, 2, 2, 2], 25),
    ],
)
def test_full_house(dice, score):
    assert kata.score_full_house(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([1, 1, 1, 1, 1], 0),
        ([1, 2, 3, 5, 6], 0),
        ([1, 2, 4, 5, 6], 0),
        ([1, 1, 2, 3, 4], 30),
        ([2, 2, 3, 4, 5], 30),
        ([3, 3, 4, 5, 6], 30),
        ([1, 2, 3, 4, 5], 30),
        ([2, 3, 4, 5, 6], 30),
    ],
)
def test_small_straight(dice, score):
    assert kata.score_small_straight(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([1, 1, 1, 1, 1], 0),
        ([1, 1, 2, 3, 4], 0),
        ([1, 2, 3, 4, 5], 40),
        ([2, 3, 4, 5, 6], 40),
    ],
)
def test_large_straight(dice, score):
    assert kata.score_large_straight(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([1, 1, 1, 1, 1], 50),
        ([1, 1, 1, 1, 2], 0),
    ],
)
def test_yahtzee(dice, score):
    assert kata.score_yahtzee(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([1, 1, 1, 1, 1], 5),
        ([1, 1, 1, 1, 2], 6),
    ],
)
def test_chance(dice, score):
    assert kata.score_chance(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ([1, 1, 1, 1, 1], 50),
        ([1, 1, 1, 1, 2], 6),
        ([1, 1, 1, 1, 6], 10),
        ([1, 1, 1, 2, 2], 25),
        ([1, 1, 1, 6, 6], 25),
        ([1, 1, 2, 2, 2], 25),
        ([1, 1, 2, 2, 3], 9),
        ([1, 1, 2, 3, 3], 10),
        ([1, 1, 2, 3, 4], 30),
        ([1, 1, 6, 6, 6], 25),
        ([1, 2, 3, 4, 5], 40),
        ([1, 2, 3, 5, 6], 17),
        ([1, 2, 4, 5, 6], 18),
        ([1, 6, 6, 6, 6], 25),
        ([2, 2, 2, 2, 2], 50),
        ([2, 2, 2, 2, 6], 14),
        ([2, 2, 2, 6, 6], 25),
        ([2, 2, 3, 4, 5], 30),
        ([2, 2, 6, 6, 6], 25),
        ([2, 3, 4, 5, 6], 40),
        ([2, 6, 6, 6, 6], 26),
        ([3, 3, 3, 3, 3], 50),
        ([3, 3, 3, 3, 6], 18),
        ([3, 3, 3, 6, 6], 25),
        ([3, 3, 4, 5, 6], 30),
        ([3, 3, 6, 6, 6], 25),
        ([3, 6, 6, 6, 6], 27),
        ([4, 4, 4, 4, 4], 50),
        ([4, 4, 4, 4, 6], 22),
        ([4, 4, 4, 6, 6], 25),
        ([4, 4, 6, 6, 6], 26),
        ([4, 6, 6, 6, 6], 28),
        ([5, 5, 5, 5, 5], 50),
        ([5, 5, 5, 5, 6], 26),
        ([5, 5, 5, 6, 6], 27),
        ([5, 5, 6, 6, 6], 28),
        ([5, 6, 6, 6, 6], 29),
        ([6, 6, 6, 6, 6], 50),
    ],
)
def test_score(dice, score):
    assert kata.score(dice) == score
