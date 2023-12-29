from itertools import combinations_with_replacement, permutations


def q1(num_rats, num_cages):
    ans = set()
    for com in combinations_with_replacement(range(4), num_rats):
        for perm in permutations(com):
            cages = [0] * num_cages
            for i in perm:
                cages[i] += 1
            cages.sort()
            ans.add(tuple(cages))
    return ans

def q2(num_rats, num_cages):
    ans = set()
    for com in combinations_with_replacement(range(4), num_rats):
        for perm in permutations(com):
            cages = [0] * num_cages
            for i in perm:
                cages[i] += 1
            ans.add(tuple(cages))
    return ans


    
def q3(num_rats, num_cages):
    numerator = set()
    for com in combinations_with_replacement(range(4), num_rats):
        for perm in permutations(com):
            cages = [0] * num_cages
            for i in perm:
                cages[i] += 1
            if 2 in cages:
                numerator.add(tuple(cages))
    denominator = q2(num_rats, num_cages)
    return len(numerator)/ len(denominator)


if __name__ == "__main__":
    num_rats = 6
    num_cages = 4
    ans1 = q1(num_rats, num_cages)
    print(f'q1: {len(ans1)}')
    ans2 = q2(num_rats, num_cages)
    print(f'q2: {len(ans2)}')
    ans3 = q3(num_rats, num_cages)
    print(f'q3: {ans3}')
