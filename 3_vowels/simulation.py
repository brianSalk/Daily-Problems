from math import comb
from random import sample, choices
# You select 10 letters at random, what is the probability that EXACTLY three letters are vowels if:
# -- letters can be selected more than once
# -- letters must be unique
# for this excercise, we are considering 'y' to be a vowel

letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiouy'
l = len(letters)
v = len(vowels)
success = 3
chosen = 10
NUM_TRIALS = 100_000

# with replacement
eq = comb(chosen,success) * (v/l)**success * ((l-v)/l)**(chosen-success)


success_count = 0
for _ in range(NUM_TRIALS):
    c = choices(letters, k=10)
    vowel_count = 0
    for each in c:
        vowel_count += each in vowels
    if vowel_count == success:
        success_count += 1

print('eq: ',eq)
print('sim:',success_count/NUM_TRIALS)

# without replacement
num = comb(v,success) * comb(l-v, chosen-success)
den = comb(l,chosen)
eq = num/den
success_count = 0

for _ in range(NUM_TRIALS):
    s = sample(letters, k=10)
    vowel_count = 0
    for each in s:
        vowel_count += each in vowels
    success_count += (vowel_count == success)

print('eq: ', eq)
print('sim:', success_count/NUM_TRIALS)
