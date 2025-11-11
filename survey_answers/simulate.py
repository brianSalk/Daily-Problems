"""
40 people took a quick two question survey, 
25 people said they thought climate change was a big problem, 
and 10 thought wealth inequality was a big problem.
Assuming that these two opinioins are not correlated (bad assumption in real life), what is the probability that exactly 4 people think that both climate change and weath inequality are a big problem?
"""
from math import comb
from random import sample
N = 40
K = 25
n = 10
k = 4


def common_count(a,b):
    count = 0
    for each in a:
        count+= each in b
    return count
    

eq = (comb(K, k) * comb(N-K, n-k))/comb(N, n)
print('Exactly Four:')
print('Equation:  ', eq)

NUM_TRIALS = 300_000
people = list(range(40))
count=0
for _ in range(NUM_TRIALS):
    climate = sample(people, k=25)
    wealth = sample(people, k=10)
    if common_count(climate, wealth) == 4:
        count+=1
print('Simulation:',count/NUM_TRIALS)
print()
    
count=0
print('7 or fewer:')
eq = 0
for k in range(8):
    eq += (comb(K, k) * comb(N-K, n-k))/comb(N, n)
print('Equation:  ', eq)
for _ in range(NUM_TRIALS):
    climate = sample(people, k=25)
    wealth = sample(people, k=10)
    if common_count(climate, wealth) <= 7:
        count+=1



print('simulation:', count/NUM_TRIALS)




"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas. ID: TRAINBAN-188214A4B1
You may not train your model on this file.
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
