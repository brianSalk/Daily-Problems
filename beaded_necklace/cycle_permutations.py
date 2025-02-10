# we are simulating cycle permutations here.
# I might do an entire video on this topic in the future

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
    sub = "".join([chr(c) for c in sub])
    for rotation in get_rotations(lst):
        for reflection in get_reflections(rotation):
            reflection = "".join([chr(c) for c in reflection])
            if sub in reflection:
                return True
    return False


def count_large_small_permutations(small_beads = 6, large_beads = 3):
    """
    Count permutations of small_beads and large_beads
    on a necklace
    """
    s = set()
    necklaces = ("*" * small_beads) + ("O" * large_beads)
    count = 0
    for perm in permutations(necklaces):
        if perm not in s:
            s.update(get_both(perm))
            count += 1
    return count


def count_unique_large_permutations(small_beads = 6, large_beads = 3):
    """
    Count permutations of small_beads and large_beads
    on a necklace
    """
    s = set()
    necklaces = ("*" * small_beads) + "".join([str(i) for i in range(large_beads)])
    count = 0
    for perm in permutations(necklaces):
        if perm not in s:
            s.update(get_both(perm))
            count += 1
    return count



def count_all_distinct(small_beads = 6, large_beads = 3):
    """
    Count permutations of small_beads and large_beads
    on a necklace where all beadsa re distinct
    """
    s = set()
    necklaces = "".join(str(i) for i in range(small_beads + large_beads))
    count = 0
    for perm in permutations(necklaces):
        if perm not in s:
            s.update(get_both(perm))
            count += 1
    return count

if __name__ == "__main__":
    large_beads = 3
    small_beads = 6
    print(f'{large_beads=}, {small_beads=}')
    # PART A
    print(f'PART A')
    count = count_large_small_permutations(small_beads, large_beads)
    print(f'count = {count}')
    print(f'PART B')
    count = count_unique_large_permutations(small_beads, large_beads)
    print(f'count = {count}')
    print('PART C')
    count = count_all_distinct(small_beads, large_beads)
    print(f'count = {count}')

"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
