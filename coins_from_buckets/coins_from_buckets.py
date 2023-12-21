# P(biased_and_from_bucket_1 | heads) = P(biased_and_from_bucket_1) * P(heads | biased_and_from_bucket_1) / P(heads)
# P(heads) = 1/2 P(heads | from_bucket_1) + 1/2 P(heads | from_bucket_2)
# P(heads | from_bucket_1) = (.5 + .5 + .8) / 3 = .6
# P(heads | from_bucket_2) = (.5 + .5 + .5 + .8) / 4 = .575
# P(heads) = 1/2 * .6 + 1/2 * .575 = .5875
# P(heads | biased_and_from_bucket_1) = 1/2 * 1/3 = 1/6
import random

class Coin:
    def __init__(self, heads_probability = 0.5):
        self.heads_probability = heads_probability
        self.is_biased = heads_probability != 0.5


    def flip(self):
        return random.random() < self.heads_probability


class Bucket:
    id = 0

    
    def __init__(self, coins):
        self.coins = coins
        self.id = Bucket.id + 1
        Bucket.id = self.id

if __name__ == '__main__':
    b1 = Bucket([Coin(), Coin(), Coin(.8)])
    b2 = Bucket([Coin(), Coin(), Coin(), Coin(.8)])
    buckets = [b1, b2]
    num_trials = 2_000_000
    success_count = 0
    bucket_1 = 0
    bucket_2 = 0
    heads_count = 0
    for _ in range(num_trials):
        bucket = random.choice(buckets)
        coin = random.choice(bucket.coins)
        if coin.flip():
            heads_count += 1
            success_count += (bucket.id == 1 and coin.is_biased)
    print(f'Probability of drawing a biased coin from bucket 1 given heads: {success_count / heads_count:.3f}')
