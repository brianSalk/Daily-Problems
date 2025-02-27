# we have F freinds waiting in a line of N people.
# how many ways can they form a line so that each of the F
# friends are standing next to another freind?
# define a new constant E=(N-F)
from itertools import permutations
from math import perm


def has_no_isolated_friend(l):
    l = ('E',) + l + ('E',)
    for i,each in enumerate(l):
        if each == 'F':
            if l[i-1] != 'F' and l[i+1] != 'F':
                return False
    return True

N=10
F=5
E=(N-F)
line = ['F']*F + ['E']*E

sim=0
eq = 6 * perm(5)**2 + perm(6,2) * perm(5)**2
print(eq)
for perm in permutations(line):
    sim += has_no_isolated_friend(perm)
print(sim)

"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
