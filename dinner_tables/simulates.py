# For the simulations we are going to assume there are 9 people at the party, the table seats 5 people and there are 3 friends
from itertools import permutations
from cycle_set import *
import math

if __name__ == "__main__":
    guests = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    s = cycle_set()
    q1_ans = math.perm(9, 5) // (5*2)
    for perm in permutations(guests, 5):
        s.add(perm)
    
    if q1_ans == len(s):
        print(f"Q1: {len(s)}")
    else:
        print(f"Q1: {len(s)} != {q1_ans}")

    s = cycle_set()
    q2_ans = (math.comb(5, 3) * math.perm(3) * math.perm(6, 2)) // (2*5)
    for perm in permutations(guests, 5):
        all_there = True
        for each in "ABC":
            if each not in perm:
                all_there = False
        if all_there:
            s.add(perm)
    
    if q2_ans == len(s):
        print(f"Q2: {len(s)}")
    else:
        print(f"Q2: {len(s)} != {q2_ans}")



    s = cycle_set()
    q3_ans = (math.perm(3) * math.perm(9-3, 5-3)) // (2)
    for perm in permutations(guests, 5):
        all_there = False
        for each in permutations("ABC"):
            friends = "".join(each)
            perm = "".join(perm)
            if friends in perm:
                all_there = True
        if all_there:
            s.add(perm)
    
    if q3_ans == len(s):
        print(f"Q3: {len(s)}")
    else:
        print(f"Q3: {len(s)} != {q3_ans}")
