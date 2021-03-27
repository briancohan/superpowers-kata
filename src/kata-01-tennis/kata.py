import random


def point(weight: float = 0.5) -> int:
    """Determine which team wins the point.

    :param weight:
        If one team is presumed to be better, assign the probablility of
        team 0 to win a given point. Default value assumes an even match
    :returns:
        index of team that wins
    """
    return int(random.random() < weight)
