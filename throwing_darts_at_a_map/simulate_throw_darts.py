# problem 1:
# probability of 2 or more of 4 darts hitting national park
# probability of all 4 darts hitting farm land
# problem 2:
# I throw 4 darts, my friend throws 3:
# probability that I hit national park 3 or fewer times and and my friend hits farm land exactly once
# problem 3:
# I throw 4 darts, my friend throws 3:
# probability that I hit national park 3 or more times or and my friend hits farm land once
# demonstrates possible unintuitive result with and vs or
import random


class Dart:

    def __init__(self):
        ...
    def throw(self):
        return random.random() * 100


if __name__ == "__main__":
    my_darts = [Dart(), Dart(), Dart(), Dart()]
    friends_darts = [Dart(), Dart(), Dart()]
    farm_land_cuttoff = 52
    national_park_cuttoff = 3.6
    count_my_hits = list(range(len(my_darts) + 1))
    count_friends_hits = list(range(len(friends_darts) + 1))
    num_trials = 1_000_000
    for _ in range(num_trials):
        national_park_hits = 0
        for dart in my_darts:
            if dart.throw() < national_park_cuttoff:
                national_park_hits += 1
        count_my_hits[national_park_hits] += 1
        my_probabilities = [count_hit / num_trials for count_hit in count_my_hits]
        farm_hits = 0
        for dart in friends_darts:
            if dart.throw() < farm_land_cuttoff:
                farm_hits += 1
        count_friends_hits[farm_hits] += 1
    friends_probabilities = [count_hit / num_trials for count_hit in count_friends_hits]
    print(f'Probability that two or more of four darts hit national park: {sum(my_probabilities[2:]):.4f}')
    print(f'Probability that all three darts hit farm land: {friends_probabilities[3]:.4f}') 
    # interesting result: the next two are about equal
    print(f'Probability that I hit national park 3 or fewer times and my friend hits farm land exactly once: {sum(my_probabilities[0:4]) * friends_probabilities[1]:.4f}')
    print(f'Probability that I hit national park 3 or more times or my friend hits farm land once: {sum(my_probabilities[3:-1]) + friends_probabilities[1]:.4f}')
