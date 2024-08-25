import enum
import re
import random


def roll(rolls, sides):
    result = []
    i = 0
    # TODO: account for negative sides, etc
    while i < rolls:
        result.append(random.randint(1, sides))
        i += 1
    print("{}".format(result))
    return sum(result)


# TODO: make more efficient--combine advantage/disadvantage (and roll()?)
def advantage(rolls, sides):
    result1 = roll(rolls, sides)
    result2 = roll(rolls, sides)
    print("advantage({}, {})".format(result1, result2))
    if result1 > result2:
        return result1
    else:
        return result2


def disadvantage(rolls, sides):
    result1 = roll(rolls, sides)
    result2 = roll(rolls, sides)
    print("disadvantage({}, {})".format(result1, result2))
    if result1 < result2:
        return result1
    else:
        return result2
