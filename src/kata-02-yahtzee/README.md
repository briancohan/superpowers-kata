# Yahtzee

The game of Yahtzee is a simple dice game. Each round, each player rolls five six-sided dice. The player may choose to roll some or all of the dice up to three times (including the original roll). The player then assigns the roll a category, such as ones, twos, sixes, one pair, two pairs, etc. If the roll is compatible with the score, the player gets a score for this roll according to the rules. If the roll is not compatible, the player gets a score of zero for this roll.

The kata consists of creating the rules to score a roll in any predefined category. Given a roll and a category, the final solution should output the score for this roll placed in this category.

The categories for Yahtzee are:

- Ones, Twos, Threes, Fours, Fives, Sixes: The player scores the sum of the dice that read one, two, three, four, five, or six, respectively. For example, 1, 1, 2, 4, 4 assigned “fours” gives 8 points.
- Three of a kind: If there are three dice with the same number, the player scores the sum of all dice. Otherwise, the player scores 0. For example, 3, 3, 3, 4, 5 assigned “three of a kind” gives 18.
- Four of a kind: If there are four dice with the same number, the player scores the sum of all dice. Otherwise, the player scores 0. For example, 2, 2, 2, 2, 5 assigned “four of a kind” gives 13.
- Small straight: If there are four sequential dice, like 1,1,2,3,4, the player scores 30, otherwise 0.
- Large straight: If all dice are sequential, the player scores 40 (the sum of all the dice), otherwise 0. 2,3,4,5,6, would score 40
- Full house: If there are two of a kind and three of a kind, the player scores 25. For example, 1,1,2,2,2 placed on “full house” gives 8. 4,4,4,4,4 is not a “full house”.
- Yahtzee: If all dice have the same number, the player scores 50 points, otherwise 0.
- Chance: The player gets the sum of all dice, no matter what they read.

Again, it’s up to you how to solve this. I encourage you to create a central function or module to solve this, and if you want to, add something more to the solution.
