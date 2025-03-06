from math import comb, perm
from itertools import combinations
from random import sample
from copy import copy

cards = list(range(2,11)) + ['J', 'K', 'Q', 'A']
cards*=4

total = 0
eq = comb(4,2)/comb(52,2)
for hand in combinations(cards, r=2):
    total += list(hand).count('A') == 2
if total/comb(52,2) == eq:
    print(eq)
else:
    print('answers do not match:', total/comb())


total = 0
eq = comb(4,2)/comb(50,2)
for hand in combinations(cards, r=2):
    total += list(hand).count('A') == 2
if total /comb(50,2) == eq:
    print(eq)
else:
    print('answers do not match:',total/comb(50,2), eq)

# if 4 people are playing textas holdem, what is the Propbability that 
NUM_TRIALS = 1_000_000
count = 0
for _ in range(NUM_TRIALS):
    cards_cp = copy(cards)
    a = sample(cards_cp,k=2)
    cards_cp.remove(a[0])
    cards_cp.remove(a[1])
    b = sample(cards_cp,k=2)
    cards_cp.remove(b[0])
    cards_cp.remove(b[1])
    c = sample(cards_cp,k=2)
    cards_cp.remove(c[0])
    cards_cp.remove(c[1])
    d = sample(cards_cp,k=2)
    cards_cp.remove(d[0])
    cards_cp.remove(d[1])
    if a == ['A', 'A'] or b == ['A','A'] or c == ['A','A'] or d == ['A','A']:
        count += 1
eq =  comb(4,2)  * comb(50,2) * comb(48,2) * comb(46,2) * 4
eq /= comb(52,2) * comb(50,2) * comb(48,2) * comb(46,2)

print()
print('equation  ', eq)
print('simulation', count/NUM_TRIALS)
    


    

