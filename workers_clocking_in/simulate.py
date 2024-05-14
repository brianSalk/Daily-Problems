import random
import copy


def matches(a, b):
    count = 0
    for i in range(9):
        count += (a[i] == b[i])
    return count


def count_successes(num_simulations, same_count):
    employees = [1,2,3,4,5,6,7,8,9]
    num_simulations = 1_000_000
    count = 0
    success = 0
    while count < num_simulations:
        old_list = copy.copy(employees)
        random.shuffle(employees)
        new_list = copy.copy(employees)
        success += (matches(old_list, new_list) == same_count)
        count += 1
    return success


if __name__ == "__main__":
    num_simulations = 1_000_000
    successes = count_successes(num_simulations, 1)
    print(
        f'Odds of getting 1 matching char: {successes / num_simulations}'
        )
    
    successes = count_successes(num_simulations, 2)
    print(
        f'Odds of getting 2 matching chars: {successes / num_simulations}'
        )
