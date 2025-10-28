from random import shuffle
from math import comb, factorial

def has_four_queens(deck):
    queen_count = 0
    for card in deck:
        if card == 'q':
            queen_count+=1 
        if card == 'k':
            return queen_count == 4
            
d = [2,3,4,5,6,7,8,9,10,'j','q','k','a']
deck = []
for each in d:
    for _ in range(4):
        deck.append(str(each))

NUM_TRIALS = 100_000
successes = 0
for _ in range(NUM_TRIALS):
    shuffle(deck)
    successes += has_four_queens(deck)
print('simulation:',successes/NUM_TRIALS)

num = 0 
den = factorial(52)
for n in range(5,50):
    num += factorial(4)**2 * comb(n-1,4) * comb(52-n,3) * factorial(44)
print('Equation:',num/den)
