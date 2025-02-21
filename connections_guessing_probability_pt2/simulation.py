import random
from collections import Counter
from math import comb

def guess_correct(num_catogories_already_guessed, num_trials):
    if num_catogories_already_guessed == 0:
        categories = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    elif num_catogories_already_guessed == 1:
        categories = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
    elif num_catogories_already_guessed == 2:
        categories = [0, 0, 0, 0, 1, 1, 1, 1]
    else:
        return 1
    correct_count = 0
    for _ in range(num_trials):
        chosen = random.sample(categories, 4)
        counts = Counter(chosen)
        if (max(counts.values()) >= 3):
            correct_count += 1
    return correct_count / num_trials
    
    
eq4 = (4*comb(4,3)*(16-4)+4)   / comb(16,4)
ans4 = guess_correct(0, 1_000_000)

"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
