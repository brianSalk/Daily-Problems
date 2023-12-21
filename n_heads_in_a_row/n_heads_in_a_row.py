# how many times, on average, would you need to flip a fair coin until you get N heads in a row?
import random
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
    num_trials = 1_000_000
    for goal in range(1,8):
        trials = 0
        for _ in range(num_trials):
            heads_count = 0
            flips_per_trial = 0 
            while heads_count < goal:
                if random.random() >= .5:
                    heads_count += 1
                else:
                    heads_count = 0
                flips_per_trial += 1
            trials += flips_per_trial
        print(f'it takes {trials/num_trials} flips to get {goal} heads in a row')
