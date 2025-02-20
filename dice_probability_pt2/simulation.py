from math import comb, factorial
from random import randint
from collections import defaultdict


def roll(n):
    dice = defaultdict(int)
    for _ in range(n):
        r = randint(1,6)
        dice[r]+=1
    return dice

def has_lstraight(d):
    return all([val in d.keys() for val in range(1,6)]
    ) or all([val in d.keys() for val in range(2,7)])

def has_sstraight(d):
    return all(val in d.keys() for val in range(1,5)
    ) or all(val in d.keys() for val in range(2,6)
    ) or all(val in d.keys() for val in range(3,7))

def has_fullhouse(d):
    return sorted(d.values()) == [2,3]

    
count_fh = count_ss = count_ls = 0

denom = 6**5

eq_ls = (2*factorial(5))/denom
eq_ss = (4*factorial(5) + 3*4*factorial(5)/2) / denom
eq_fh = 6*5*comb(5,3)/ denom


NUM_TRIALS = 500_000
for _ in range(NUM_TRIALS):
    d = roll(5)
    count_fh += has_fullhouse(d)
    count_ss += has_sstraight(d)
    count_ls += has_lstraight(d)
    
print(f'P(large straight): simulation={count_ls/NUM_TRIALS:.3f},  equation={eq_ls:.3f}')
print(f'P(small straight): simulation={count_ss/NUM_TRIALS:.3f},  equation={eq_ss:.3f}')
print(f'P(full house): simulation={count_fh/NUM_TRIALS:.3f},  equation={eq_fh:.3f}')

"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
