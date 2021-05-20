import random

def strategy(history, memory):
    mem = false
    choice = 1
    if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
        choice = 0
        mem = false
    if memory and random.randint(0,100) < 20:
        choice = (choice + 1) * -1
        mem = true
    return choice, mem
