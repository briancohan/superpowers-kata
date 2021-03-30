"""Simulate tennis matches

The growth challenge kata suggests simulating a single game and calling out
the score. However, I wanted to go a little extra and do game-set-match.

For official tennis terminology and rules:
https://www.usta.com/en/home/improve/tips-and-instruction/national/tennis-scoring-rules.html
"""
from __future__ import annotations
import random
from itertools import cycle


SCORE = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}
SERVER = cycle([0, 1])


def point(weight: float = 0.5) -> int:
    """Determine which team wins the point.

    :param weight:
        If one team is presumed to be better, assign the probablility of
        team 0 to win a given point. Default value assumes an even match
    :returns:
        index of team that wins
    """
    return int(random.random() < weight)


def announce(scores: list[int]) -> str:
    """Announce current score of the game.

    :param scores:
        List of two integers representing the number of points by each player.
        Server score is listed first.
    :returns:
        String indicating score.
    """
    if scores[0] == scores[1]:
        if scores[0] < max(SCORE):
            return f"{SCORE[scores[0]]} All"
        else:
            return "Deuce"

    if max(scores) <= max(SCORE):
        return f"{SCORE[scores[0]]}-{SCORE[scores[1]]}"

    if abs(scores[0] - scores[1]) == 1:
        if scores[0] > scores[1]:
            return "Advantage Server"
        else:
            return "Advantage Receiver"

    if scores[0] > scores[1]:
        return "Server Wins"
    else:
        return "Receiver Wins"


def game(weight: float = 0.5) -> tuple[int, list[str]]:
    """Simulate a game of tennis.

    :param weight:
        If one team is presumed to be better, assign the probablility of
        team 0 to win a given point. Default value assumes an even match
    :returns:
        - int: index of team that wins
        - list[str]: score announcements
    """
    scores = [0, 0]
    annoucements = []
    while True:
        scores[point(weight=weight)] += 1
        annoucements.append(announce(scores))
        if "Win" in annoucements[-1]:
            winner = scores.index(max(scores))
            return winner, annoucements


def game_set(weight: float = 0.5) -> tuple[int, list[int]]:
    """Simulate a set of games.

    Logic follows the 'advantage set' rules where the winner must
    win by at least two games.

    :param weight:
        If one team is presumed to be better, assign the probablility of
        team 0 to win a given point. Default value assumes an even match
    :returns:
        - int: index of team that wins
        - list[int]: scores
    """
    scores = [0, 0]
    while True:
        serving = next(SERVER)
        _weight = weight if serving == 0 else 1 - weight
        winner, announcements = game(weight=_weight)

        winner_ix = (winner + serving) % 2
        scores[winner_ix] += 1

        if max(scores) >= 6 and abs(scores[0] - scores[1]) > 2:
            winner = scores.index(max(scores))
            return winner, scores
