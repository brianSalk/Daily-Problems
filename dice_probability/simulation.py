from random import randint
from collections import defaultdict
from math import comb

def roll(n):
    dice = defaultdict(int)
    for _ in range(n):
        r = randint(1,6)
        dice[r]+=1
    return dice


NUM_TRIALS = 1_000_000
NUM_DICE=5
count3=count4=count5=0

denom = 6**NUM_DICE
eq5=6/denom
eq4=(6*5**2)/denom
eq3=(6*comb(5,2)*5**2)/denom
eq3 += eq4+eq5

for _ in range(NUM_TRIALS):
    r = roll(NUM_DICE)
    m = max(r.values())
    count5+= m==5
    count4+= m==4
    count3+= m>=3

print(f'P(5 of kind): simulation={count5/NUM_TRIALS:.5f}, equation={eq5:.5f}')
        
print(f'P(4 of kind): simulation={count4/NUM_TRIALS:.5f}, equation={eq4:.5f}')

print(f'P(>=3 of kind): simulation={count3/NUM_TRIALS:.4f}, equation={eq3:.4f}')
