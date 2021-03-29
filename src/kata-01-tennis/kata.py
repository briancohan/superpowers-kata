import random

SCORE = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}


def point(weight: float = 0.5) -> int:
    """Determine which team wins the point.

    :param weight:
        If one team is presumed to be better, assign the probablility of
        team 0 to win a given point. Default value assumes an even match
    :returns:
        index of team that wins
    """
    return int(random.random() < weight)


def announce(scores) -> str:
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
