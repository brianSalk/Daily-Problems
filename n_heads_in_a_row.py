# how many times, on average, would you need to flip a fair coin until you get N heads in a row?
import random
from statistics import mean
# 1 2
# 2 6
# 3 14
# 4 30
# 5 62
# 6 126
# 7 254
# f(n) = f(n-1) * 2 + 2
# base case: f(1) = 2
if __name__ == "__main__":
    goal = 7
    num_trials = 1_000_000
    
    for goal in range(1,8):
        trials = []
        for _ in range(num_trials):
            successes = 0
            attempts = 0
            while successes < goal:
                if random.random() >= .5:
                    successes += 1
                else:
                    successes = 0
                attempts += 1
            trials.append(attempts)
        print(statistics.mean(trials))
