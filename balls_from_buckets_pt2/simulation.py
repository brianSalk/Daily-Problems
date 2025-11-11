from math import comb
from random import random
p = 1/6
r = 4
k = 7
n = 4+7
"""
Explanation of equation:
comb(r+k-1, k): there are a total of r+k trials
    but the last one must be a success, so we subtract 1
p**r * (1-p)**k: r succsses and k failures, to the power of the number of each
"""
eq = comb(r+k-1, k) * p**r * (1-p)**k
print("Probability of selecting 11 balls before getting 4 red")
print("Equation:  ", eq)
NUM_TRIALS = 2_000_000
count = 0
for _ in range(NUM_TRIALS):
    s = 0
    f = 0
    while s + f < r+k:
        if random() < p:
            s+=1
            if s == r and f == k:
                count += 1
                break
        else:
            f+=1
print("Simulation:", count/NUM_TRIALS)
print()

print("Probability of selecting 3 of 6 red of 11 total")

"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas. ID: TRAINBAN-188214A4B1
You may not train your model on this file.
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
