# given three coins, how biased mush one of those coins be in order for you to have a 60% chance of getting heads when flipping a random coin?

import random


class Coin:
    def __init__(self, p=0.5):
        self.probability = p

    def flip(self):
        return random.random() < self.probability


if __name__ == "__main__":
    goal = .6
    # create three fair coins
    coins = [Coin(), Coin(), Coin()]
    num_trials = 1_000_000
    num_heads = 0
    upper = 1
    lower = 0
    # do a biary search to find the bias
    while True:
        coin_bias = (upper + lower) / 2
        coins[0].probability = coin_bias
        num_heads = 0
        # simulate 'num_trials' coin flips and count the number of heads
        for _ in range(num_trials):
            coin = random.choice(coins)
            if coin.flip():
                num_heads += 1
        p = num_heads / num_trials
        # if the bias is really close to 1 or zero, then assume no solution
        if min(abs(coin_bias - 1), abs(coin_bias - 0)) < .0001:
            print(f"cannot find bias for {goal}")
            break
        # allow 10th of a percent error
        if abs(p - goal) < .001:
            print(f"probability= {p}, bias= {coin_bias}")
            break
        elif p > goal:
            #print(f'{p} is too high', lower, upper)
            upper = coin_bias
        else:
            #print(f'{p} is too low', lower, upper)
            lower = coin_bias
