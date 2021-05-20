import random

def strategy(history, memory):
    if memory == None:
        memory = 0

    choice = 1

    if memory >= 5 or history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
        choice = 0
        memory = memory + 1

        if len(history[0]) % 50 == 0:
            memory = 0


    return choice, memory
