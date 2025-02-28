from itertools import permutations
from math import comb, perm

eq_total = int(perm(9)/(perm(3)**3))

total = set()
balls = list(range(9))
for p in permutations(balls):
    buckets = [[],[],[]]
    buckets[0] = tuple(sorted(p[0:3]))
    buckets[1] = tuple(sorted(p[3:6]))
    buckets[2] = tuple(sorted(p[6:9]))
    total.add(tuple(buckets))

print('total')
print(len(total))
print(eq_total)

print('bobby and billy not next to eachother:')
has_two_next = 0
for b in total:
    is_good = True
    for each in b:
        if 1 in each and 2 in each:
            is_good = False
            break
    
print(len(total))
