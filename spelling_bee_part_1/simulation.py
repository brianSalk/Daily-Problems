import itertools
import math


def count_spelling_bees():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for middle in alphabet:
        for outer_letters in itertools.combinations(alphabet, 6):
            count += middle not in outer_letters
    return count

if __name__ == "__main__":
    simulation_answer = count_spelling_bees()
    answer = math.comb(25, 6) * 26 # approach 1
    answer2 = math.comb(26, 7) * 7 # approach 2
    
    if simulation_answer == answer == answer2:
        print(f"there are {answer:,} unique spelling bees")
    else:
        print(f"{simulation_answer:,}, {answer:,}, and {answer2:,} are not equal")
