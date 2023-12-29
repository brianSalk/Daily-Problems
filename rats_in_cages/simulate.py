from itertools import combinations_with_replacement, permutations

def q1(num_people, num_cages):
    ans = set()
    for com in combinations_with_replacement(range(4), 6):
        for perm in permutations(com):
            cages = [0] * num_cages
            for i in perm:
                cages[i] += 1
            cages.sort()
            ans.add(tuple(cages))
    print(ans)
    print(len(ans))


def q2(num_people, num_cages):
    ans = set()
    for com in combinations_with_replacement(range(4), 6):
        for perm in permutations(com):
            cages = [0] * num_cages
            for i in perm:
                cages[i] += 1
            ans.add(tuple(cages))
    print(ans)
    print(len(ans))

if __name__ == "__main__":
    num_rats = 6
    num_cages = 4
    q1(num_rats, num_cages)
    q2(num_rats, num_cages)

        

