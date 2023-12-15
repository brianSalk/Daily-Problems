# we are choosing 1 of 5 coins at random
# one of the coins has a 90% chance of coming up heads, the rest are fair
# Given that we flipped heads, what is the probability that we chose the biased coin?

import random


class Coin:
    def __init__(self, heads_probability):
        self.heads_probability = heads_probability
        self.is_biased = heads_probability != 0.5

    def flip(self):
        return random.random() < self.heads_probability


if __name__ == "__main__":
    num_trials = 1_000_000
    coins = [Coin(.5) for _ in range(4)] + [Coin(.9)]
    head_count = 0
    biased_coin_count = 0
    while True:
        coin_chosen = random.choice(coins)
        result = coin_chosen.flip()
        if result:
            head_count += 1
            if coin_chosen.is_biased:
                biased_coin_count += 1
        if biased_coin_count == num_trials:
            break
    print(f"Probability of coin being biased given heads: {biased_coin_count/head_count}")
