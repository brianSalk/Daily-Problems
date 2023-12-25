#question 1 1 of three darts hit water, 2 or four hit land
#question 2: probability 3 or more of 5 darts hit water
# question 3, each dart has a 70% chance of hitting the map
# find probability of hitting the map and hitting land AT MOST
# 4 times out of 6 throws

import random

if __name__ == "__main__":
    #q1
    num_trials = 1_000_000
    land_water_cuttoff = .71
    num_blue_darts = 3
    num_green_darts = 4
    num_success = 0
    for _ in range(num_trials):
        num_blue_hits = 0
        num_green_hits = 0
        for throw in range(num_blue_darts):
            if random.random() < land_water_cuttoff:
                num_blue_hits += 1
        for throw in range(num_green_darts):
            if random.random() > land_water_cuttoff:
                num_green_hits += 1
        if num_blue_hits == 1 and num_green_hits == 2:
            num_success += 1
    print(f"Q1: Probability of 1 of 3 darts hitting water and 2 or 4 hitting land: {num_success/num_trials}")
    num_success = 0
    for _ in range(num_trials):
        num_hits = 0
        for throw in range(6):
            if random.random() < land_water_cuttoff:
                num_hits += 1
        if num_hits >= 3:
            num_success += 1
    print(f"Q2: Probability of 3 or more of 6 darts hitting water: {num_success/num_trials}")
    num_darts = 6
    prob_hit_map = .7
    total_num_hits = 0
    for _ in range(num_trials):
        num_hits = 0
        for throw in range(num_darts):
            if random.random() < prob_hit_map:
                if random.random() > land_water_cuttoff:
                    num_hits += 1
        if num_hits <= 4:
            total_num_hits += 1
    print(f"Q3: Probability of hitting map and land at most 4 times out of 6 throws: {total_num_hits/num_trials}")
