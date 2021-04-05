from __future__ import annotations
from random import randint
import functools
from collections import Counter
import inspect
import sys


class KataError(Exception):
    """Example base class error for anything in this kata."""

    pass


class InvalidRoll(KataError):
    """The roll did not have the required number of dice."""

    pass


class InvalidDie(KataError):
    """A die rolled a value higher than expected."""

    pass


def valid_roll(n_dice: int = 5, sides: int = 6):
    """Ensure the roll represents n d-sided dice.

    :param n_dice:
        Number of dice expected in the roll
    :param sides:
        Number of sides on each die (assumed to all be of the same type)
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            dice = kwargs.get("dice", None)
            if args and dice is None:
                dice = args[0]
            if dice is None:
                dice = []

            if len(dice) != n_dice:
                raise InvalidRoll(f"You must roll {n_dice} dice, received {len(dice)}")
            values = list(range(1, sides + 1))
            for die in dice:
                if die not in values:
                    raise InvalidDie(f"You rolled an invalid die {die}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def roll(n_dice: int):
    """Roll a given number of dice.

    :param n_dice:
        Number of dice to roll
    """
    return [randint(1, 6) for _ in range(n_dice)]


@valid_roll()
def _score_all_of_kind(dice: list[int], value: int) -> int:
    """Score all dice of a given kind.

    :param dice:
        List of five dice
    :param value:
        value that a die must show to be scored
    """
    return sum([d for d in dice if d == value])


@valid_roll()
def score_ones(dice: list[int]) -> int:
    """Score sum of all dice with a value of 1.

    :param dice:
        List of five dice
    """
    return _score_all_of_kind(dice, 1)


@valid_roll()
def score_twos(dice: list[int]) -> int:
    """Score sum of all dice with a value of 2.

    :param dice:
        List of five dice
    """
    return _score_all_of_kind(dice, 2)


@valid_roll()
def score_threes(dice: list[int]) -> int:
    """Score sum of all dice with a value of 3.

    :param dice:
        List of five dice
    """
    return _score_all_of_kind(dice, 3)


@valid_roll()
def score_fours(dice: list[int]) -> int:
    """Score sum of all dice with a value of 4.

    :param dice:
        List of five dice
    """
    return _score_all_of_kind(dice, 4)


@valid_roll()
def score_fives(dice: list[int]) -> int:
    """Score sum of all dice with a value of 5.

    :param dice:
        List of five dice
    """
    return _score_all_of_kind(dice, 5)


@valid_roll()
def score_sixes(dice: list[int]) -> int:
    """Score sum of all dice with a value of 6.

    :param dice:
        List of five dice
    """
    return _score_all_of_kind(dice, 6)


@valid_roll()
def score_3_of_kind(dice: list[int]) -> int:
    """Sum dice if at least 3 of them are the same.

    :param dice:
        List of five dice
    """
    value, count = Counter(dice).most_common()[0]
    if count >= 3:
        return sum(dice)
    return 0


@valid_roll()
def score_4_of_kind(dice: list[int]) -> int:
    """Sum dice if at least 4 of them are the same.

    :param dice:
        List of five dice
    """
    value, count = Counter(dice).most_common()[0]
    if count >= 4:
        return sum(dice)
    return 0


@valid_roll()
def score_full_house(dice: list[int]) -> int:
    """Sum dice if there is three of one number and two of another.

    :param dice:
        List of five dice
    """
    roll = Counter(dice)
    if len(roll) == 2 and roll.most_common()[0][1] == 3:
        return 25
    return 0


@valid_roll()
def score_small_straight(dice: list[int]) -> int:
    """Score 30 points if there is a run of 4 consecutive dice.

    :param dice:
        List of five dice
    """
    for low in range(1, 4):
        if len(set(dice).intersection(range(low, low + 4))) == 4:
            return 30
    return 0


@valid_roll()
def score_large_straight(dice: list[int]) -> int:
    """Score 40 points if there is a run of 5 consecutive dice.

    :param dice:
        List of five dice
    """
    roll = Counter(dice)
    if len(roll) == 5 and len({2, 3, 4, 5}.intersection(dice)) == 4:
        return 40
    return 0


@valid_roll()
def score_yahtzee(dice: list[int]) -> int:
    """Score 50 points if all the dice are the same.

    :param dice:
        List of five dice
    """
    value, count = Counter(dice).most_common()[0]
    if count == 5:
        return 50
    return 0


@valid_roll()
def score_chance(dice: list[int]) -> int:
    """Sum of all dice.

    :param dice:
        List of five dice
    """
    return sum(dice)


@valid_roll()
def score(dice: list[int]) -> int:
    """Find the best score for the given roll.

    Identifies all functions in the current module that starts with `score_`
    and gets the score for that condition. Returns the highest of all
    possible scores for a given roll.

    :param dice:
        List of five dice
    """
    scores = [
        func(dice)
        for name, func in inspect.getmembers(sys.modules[__name__])
        if inspect.isfunction(func)
        and inspect.getfile(func) == __file__
        and name[:6] == "score_"
    ]
    return max(scores)
