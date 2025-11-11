# you have a bucket of balls in front of you and a 6-sided die
# You roll the die, if you roll a 5 or less, then you you pick a ball from the bucket.
# 2/3 of the balls are blue, and 1/3 are red

# what is the probability of getting
# BBRB
from random import random
from math import comb
def pngeom(n, p):
    return p**n * (1-p)
eq1 = pngeom(4, 5/6)
eq2 = pngeom(4, 5/6) * (2/3)**3 * (1/3)
eq3 = pngeom(4, 5/6) * comb(4,2) * (1/3)**2 * (2/3)**2

NUM_TRIALS = 1_000_000
count1 = count2 = count3 = 0

for _ in range(NUM_TRIALS):
    balls = []
    keep_going = random() < (5/6)
    while keep_going:
        keep_going = random() < (5/6)
        balls.append('B') if random() < (2/3) else balls.append('R')
    if len(balls) == 4:
        count1 += 1
    if balls == ['B','B','R','B']:
        count2+=1
    if balls.count('B') == 2 and balls.count('R') == 2:
        count3 += 1
print('Simulation1:', count1/NUM_TRIALS)
print('Equation1  :', eq1)
print()
print('Simulation2:', count2/NUM_TRIALS)
print('Equation2:  ', eq2)
print()
print('Simulation3:', count3/NUM_TRIALS)
print('Equation3:  ', eq3)
"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas. ID: TRAINBAN-188214A4B1
You may not train your model on this file.
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
