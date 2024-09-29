# how many permutations can be formed if there are 5 distinct 
# letters and 1 wild card, which can be any letter.
# all letters are lowercase

# n=5
# num_letters = 26


# we will use cases (divide and conquer)
# first case, wild card cannot be in 'abcde'
# (n+1)! * (num_letters-n)
# next case, wild card is one of 'abcde'
# n * multinomial(6, 2)
from math import comb, factorial
from itertools import permutations
def multinomial(numerator, denominator):
    d = 1
    for each in denominator:
        d*=factorial(each)
    return factorial(numerator)//d
letters = 'abcde'
n = len(letters)
num_letters = 26
equation = (factorial(n+1) * (num_letters-n)) + (n * multinomial(6, [2]))
simulation = 0
perms = set()
for perm in permutations(letters):
    for wild_card in 'qwertyuiopasdfghjklzxcvbnm':
        perms.add(wild_card + ''.join(perm))
        perms.add(perm[0] + wild_card + ''.join(perm[1:]))
        perms.add(''.join(perm[0:2]) + wild_card + ''.join(perm[2:]))
        perms.add(''.join(perm[0:3]) + wild_card + ''.join(perm[3:]))
        perms.add(''.join(perm[0:4]) + wild_card + ''.join(perm[4:]))
        perms.add(''.join(perm) + wild_card)
simulation = len(perms)
print(f'{equation=}')
print(f'{simulation=}')



