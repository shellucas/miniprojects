import random

lowBound = int(input('What is the lower bound of the dice? '))
highBound = int(input('What is the higher bound of the dice? '))

dice = [x for x in range(lowBound, highBound + 1)]


def roll():
    return random.sample(dice, 1)


print(roll())
