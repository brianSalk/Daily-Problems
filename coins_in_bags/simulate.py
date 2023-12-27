# coins in bags
# all coins are unique, all bags are unique
# q1: each coin gets placed into a bag
# q2: each coin must be placed into a bag, and each bag must have at least one coin
import itertools


def q1():
    combinations = set()
    for index_com in itertools.combinations_with_replacement(range(3), 5):
        for index_perm in itertools.permutations(index_com):
            bags = [[], [], []]
            for i, bag_i in enumerate(index_perm):
                bags[bag_i].append(coins[i])
            a, b, c = bags
            ts = (tuple(sorted(a)), tuple(sorted(b)), tuple(sorted(c)))
            combinations.add(ts)

    return combinations

def q2():
    combinations = set()
    for index_com in itertools.combinations_with_replacement(range(3), 5):
        for index_perm in itertools.permutations(index_com):
            bags = [[], [], []]
            for i, bag_i in enumerate(index_perm):
                bags[bag_i].append(coins[i])
            a, b, c = bags
            if len(a) >= 1 and len(b) >= 1 and len(c) >= 1:
                ts = (tuple(sorted(a)), tuple(sorted(b)), tuple(sorted(c)))
                combinations.add(ts)

    return combinations

def q3():
    combinations = set()
    for index_com in itertools.combinations_with_replacement(range(4), 5):
        for index_perm in itertools.permutations(index_com):
            bags = [[], [], []]
            for i, bag_i in enumerate(index_perm):
                if index_perm[i] < 3:
                    bags[bag_i].append(coins[i])
            a, b, c = bags
            if len(a) <= 1 and len(b) <= 1 and len(c) <= 1:
                ts = (tuple(sorted(a)), tuple(sorted(b)), tuple(sorted(c)))
                combinations.add(ts)


    return combinations  

def q4():
    combinations = set()
    for index_com in itertools.combinations_with_replacement(range(4), 5):
        for index_perm in itertools.permutations(index_com):
            bags = [[], [], []]
            for i, bag_i in enumerate(index_perm):
                if index_perm[i] < 3:
                    bags[bag_i].append(coins[i])
            a, b, c = bags
            if len(a) == 1 and len(b) == 1 and len(c) == 1:
                ts = (tuple(sorted(a)), tuple(sorted(b)), tuple(sorted(c)))
                combinations.add(ts)
    return combinations
if __name__ == "__main__":
    coins = [1, 5, 10, 25, 100]
    ans = q1()
    print(len(ans))
    ans = q2()
    print(len(ans))
    ans = q3()
    print(len(ans))
    ans = q4()
    print(len(ans))
