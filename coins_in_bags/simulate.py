# coins in bags
# all coins are unique, all bags are unique
# q1: each coin gets placed into a bag
# q2: each coin must be placed into a bag, and each bag must have at least one coin


if __name__ == "__main__":
    coins = [1, 5, 10, 25, 100]
    bags = ['small', 'medium', 'large']

    # how many ways can we distribute the coins into the bags?
    combinations = set()
    for coin in coins:
        for bag in bags:
            combinations.add((coin, bag))
    print(f'there are {len(combinations)} ways to distribute {len(coins)} coins into {len(bags)} bags')
    # now we require that each bag has at least one coin
    combinations = set()
    for coin in coins:
        for bag in bags:
            combinations.add((coin, bag))
