# Submitted by Matteo Gaudio, matteog1999@gmail.com, MatteoG195@github
# Strategy: memory keeps track of slights against the user, after 3 strikes
# reverts to alwaysDefect. Every 25 rounds the opponent's count is reset.

import random

def strategy(history, memory):
    if memory == None:
        memory = 0

    choice = 1

    if memory >= 3 or history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
        choice = 0
        memory = memory + 1

    return choice, memory
