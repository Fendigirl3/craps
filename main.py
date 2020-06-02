#-------------------------------------------------------------------#
#                       Simulation of Craps                         #
#-------------------------------------------------------------------#

import random

N = 10000  # number of replications

# global variables
# long    i                                 # replication index
# long    point                             # the initial roll
# long    result                            # 0 = lose, 1 = win
wins = 0  # number of wins


# double  p                                 # probability estimate
# ------------------------------
def Equilikely(a, b):  # use a < b
    # ------------------------------
    return (a + int((b - a + 1) * random.random()))


# --------------
def Roll():
    # --------------
    return (Equilikely(1, 6) + Equilikely(1, 6))


# --------------------                # roll until a 7 is obtained
def Play(point):                      #  - then return a 0
    # --------------------            # or the point is made
                                      #  - then return a 1
    condition = True
    while (condition == True):
        sum = Roll()
        condition = (sum != point) and (sum != 7)

    if (sum == point):
        return (1)
    else:
        return (0)


#----------------------- Main Program -----------------------#
random.seed(0)

for i in range(0, N):  # do N Monte Carlo replications
    point = Roll()
    if (point in [7, 11]):
        result = 1
    elif (point in [2, 3, 12]):
        result = 0
    else:
        result = Play(point)

    wins += result

p = float(wins) / float(N)  # estimate the probability of winning
q = 1 - p  # estimate the probability of losing

print("Welcome to Craps! Here, we will calculate the probability of winning or\nlosing in the game of craps.")
print("\nFor {0:1d} replications: ".format(N))
print("\nThe estimated probability of winning is: {0:5.3f}\n".format(p))
print("The estimated probability of losing is: ", q, "\n")

# Which bet has the highest probability of winning?
print("-----------------------------------------")
print("\nIn a casino, the game of craps is typically played with a table layout\nwhere one can place bets on the Pass Line and Don't Pass line.")
print("\nWhich is the best bet to make in order to win?\n")
print("The probability of winning is: ", p, "\nand the probability of losing is: ", q)
print("\nBased on these probabilities, it is better in the long run to bet that\nthe player will lose, or in other words bet on the Don't Pass line.\n")

# C output:
# Enter a positive integer seed (9 digits or less) >> 123456789

# i.e.,
# for 10000 replications
# the estimated probability of winning is 0.485
# the estimated probability of losing is
