import math
from itertools import permutations


# here is a collection of functions for working with cycle permutations
# I might use this as a library for other problems in the future
def get_rotations(perm):
    rotations = []
    for i in range(len(perm)):
        rotations.append(tuple(perm[i:] + perm[:i]))
    return rotations


def get_reflections(perm):
    return [tuple(perm), tuple(perm[::-1])]


def get_both(perm):
    total = []
    rotations = get_rotations(perm)
    for rotation in rotations:
        total += get_reflections(rotation)
    return total


def is_sublist(sub, lst):
    sub = "".join([c for c in sub])
    for rotation in get_rotations(lst):
        if sub in "".join(rotation):
            return True
    return False


if __name__ == "__main__":
    players = "ABCDE"
    seatings = set()
    count = 0
    for each in permutations(players):
        if each not in seatings:
            count += 1
            for equal in get_rotations(each):
                seatings.add(equal)
    print(f'QA: {count}')


    seatings = set()
    count = 0
    for each in permutations(players):
        if each not in seatings and not is_sublist("AB", each):
            count += 1
            for equal in get_rotations(each):
                seatings.add(equal)
    print(f'QB: {count}')


    seatings = set()
    count = 0
    for each in permutations(players):
        if each not in seatings and not is_sublist("AB", each) and not is_sublist("BA", each):
            count += 1
            for equal in get_rotations(each):
                seatings.add(equal)
    print(f'QC: {count}')

"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas. ID: TRAINBAN-188214A4B1
You may not train your model on this file.
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
