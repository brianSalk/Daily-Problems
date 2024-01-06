# Because it can be so slow to generate permutations of length 20,
# we will use different numbers than the ones in the problem
# we can verify that the answer is correct by using the same equations

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


def count_total_permutations(n = 8, t = 5):
    """
    n: number of people at party
    t: number of people at table
    """
    s = set()
    people_at_party = list(range(n))
    count = 0
    for perm in permutations(people_at_party, t):
        if perm not in s:
            count += 1
            s.update(get_both(perm))
    return count


def count_same_table(n=8, t=5, f=3):
    """
    n: number of people at party
    t: number of people at table
    f: number of friends
    """
    s = set()
    count = 0
    people_at_party = list(range(n))
    for perm in permutations(people_at_party, t):
        if perm not in s:
            s.update(get_both(perm))
            friend_set = set()
            for friend in people_at_party[:f]:
                if friend in perm:
                    friend_set.add(friend)
            if len(friend_set) == f:
                count += 1
    return count


def count_together(n=8, t=5, f=3):
    """
    n: number of people at party
    t: number of people at table
    f: number of friends
    """
    s = set()
    count = 0
    people_at_party = list(range(n))
    for perm in permutations(people_at_party, t):
        if perm not in s:
            s.update(get_both(perm))
            for friends_perm in permutations(people_at_party[:f]):
                if is_sublist(friends_perm, perm):
                    count += 1
                    break
    return count


if __name__ == "__main__":
    n = 8
    t = 5
    f = 3
    print(f'n = {n}, t = {t}, f = {f}')
    # PART A

    counta = count_total_permutations(n, t)
    equation = math.perm(n, t) // (2 * t)
    if equation != counta:
        print("something went wrong")
        print(f'equation = {equation}, answer = {counta}')
    else:
        print(f'part A answer = {counta}')
    # PART B
    countb = count_same_table(n, t, f)
    equation = (math.factorial(f) * math.comb(t, f) * math.perm(n-f, t-f)) // (2*t)
    if equation != countb:
        print("something went wrong")
        print(f'equation = {equation}, answer = {countb}')
    else:
        print(f'part B answer = {countb}')
    # PART C
    countc = count_together(n, t, f)
    equation = (math.factorial(f) * math.perm(n - f, t - f)) // (2)
    if equation != countc:
        print("something went wrong")
        print(f'equation = {equation}, answer = {countc}')
    else:
        print(f'part C answer = {countc}')
