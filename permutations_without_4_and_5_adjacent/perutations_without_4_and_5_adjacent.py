# count the number of permutations of 1-10 where 4 and 5 are not adjacent
from itertools import permutations

if __name__ == "__main__":
    numbers = [str(i) for i in range(1, 11)]
    count = 0
    for perm in permutations(numbers):
        perm = "".join(perm)
        if "45" not in perm and "54" not in perm:
            count += 1

    print(f'there are {count:,} permutations where 4 and 5 are not adjacent')
