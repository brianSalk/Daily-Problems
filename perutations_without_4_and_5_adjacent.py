from itertools import permutations

if __name__ == "__main__":
    numbers = list(range(1, 11))
    count = 0
    for perm in permutations(numbers):
        index_of_4 = perm.index(4)
        if index_of_4 == 0 and perm[1] == 5:
            continue
        elif index_of_4 == 9 and perm[8] == 5:
            continue
        if 0 > index_of_4 < 9 and (perm[index_of_4 - 1] == 5 or perm[index_of_4 + 1] == 5):
            continue
        count += 1

    print(f'there are {count:,} permutations where 4 and 5 are not adjacent')
