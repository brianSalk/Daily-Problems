# This is one of those where we need to make our
# example smaller for the simulation.  
# Some numbers are just too big and take too long to
# simulate

# number of people = 9
# number of groups = 3
# group size = 3

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

print('bobby and billy not next to each other:')
not_together = 0
eq_not_together = int(len(total) * (6/8))
for b in total:
    is_good = True
    for each in b:
        if 1 in each and 2 in each:
            is_good = False
            break
    not_together+=is_good

if eq_not_together == not_together:
    print(eq_not_together)
else:
    print('simulation does not match equation:',
        eq_not_together, not_together)

print('Two people in same group')
are_together = 0
eq_are_together =  int(eq_total * (2/(2*3 + 2)))
for b in total:
    is_good = False
    for each in b:
        if 1 in each and 2 in each:
            is_good = True
            break
    are_together+=is_good

if eq_are_together == are_together:
    print(eq_are_together)
else:
    print('simulation does not match equation:',
        f'{eq_are_together=}, {are_together=}')

print('person is in group 1 or 2:')
in_1_or_2 = 0
eq_in_1_or_2 = int(len(total) * (2/3))
for b in total:
    for i, each in enumerate(b):
        if i in (0,1) and 0 in each:
            in_1_or_2 += 1
            break

if in_1_or_2 == eq_in_1_or_2:
    print(in_1_or_2)
else:
    print('simulation does not match equation', in_1_or_2, eq_in_1_or_2)

l = list(range(1,13))

s = set()
count = 0
print("Three in same group:")
for p in permutations(l, r=8):
    a = p[:4]
    b = p[4:8]
    s.add(
        (
            tuple(sorted(a)), 
            tuple(sorted(b))
        )
        )
c = 0
for each in s:
    a = each[0]
    b = each[1]
    if 1 in a and 2 in a and 3 in a:
        count+=1
    elif 1 in b and 2 in b and 3 in b:
        count+=1
    z = a + b
    if 1 not in z and 2 not in z and 3 not in z:
        count += 1
    c+=1
eq = (perm(12)/(perm(4)**3)) * (3*comb(4,3)/comb(12,3))
if eq == count:
    print(count)
else:
    print(f'{count=} does not equal {eq=}')
"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
