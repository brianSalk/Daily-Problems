"""
Simulate writing name with letters out of order and letters forwards or backwards.
Since I cannot progamatically write letters backwards, we use upper and lower case.
"""

from itertools import permutations, combinations
from math import comb, factorial
from copy import copy


if __name__ == '__main__':
    name = 'brian'
    names = set()
    for perm in permutations(name):
        perm = list(perm)
        for n in range(len(name)):
            for cmb in combinations(range(len(name)),r=n):
                perm_og = copy(perm)
                for i in cmb:
                    if perm[i] != 'i':
                        perm_og[i] = perm_og[i].upper()
                names.add(tuple(perm_og))
                
    eq = factorial(5) * 2**4
    if eq != len(names):
        print(f'{eq} does not equal {len(names)}')
    else:
        print(eq)
"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
