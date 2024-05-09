# Created by Brian Salkas

# pick 7 distinct English letters from the 25 letters ('s' is excluded)
# one letter goes in the center, the order of the other letters do not matter
# at least 1 of the selected letters must be a vowel

import math
import itertools


def count_unique_spelling_bees(alphabet, vowels, consonants):
    def has_at_least_one_vowel(other_six, middle, vowels):
        for vowel in vowels:
            if vowel in other_six or vowel == middle:
                return True
        return False

    simulation_answer = 0
    for middle in alphabet:
        for other_six in itertools.combinations(alphabet, 6):
            if middle not in other_six:
                simulation_answer += has_at_least_one_vowel(other_six, middle, vowels)
    return simulation_answer


if __name__ == "__main__":
    alphabet = (
        "abcdefghijklmnopqrtuvwxyz"  # remember that 's' is never used in spelling bees
    )
    vowels = "aeiou"  # vowels do not include 'y' and 'w'
    consonants = "bcdfghjklmnpqrtvwxyz"

    simulation_answer = count_unique_spelling_bees(alphabet, vowels, consonants)

    num_letters = len(alphabet)
    num_vowels = len(vowels)
    num_consonants = len(consonants)
    num_outer_letters = 6
    # first count how many ways a spelling bee can be created with a vowel in the middle
    vowel_in_middle = num_vowels * math.comb(num_letters - 1, 6)
    # next count how many ways a speeling bee can be created with a consonant in the middle
    consonant_in_middle = num_consonants * (
        math.comb(num_letters - 1, 6) - math.comb(num_letters - 1 - num_vowels, 6)
    )
    # add both of those solutions together
    answer = vowel_in_middle + consonant_in_middle

    if simulation_answer == answer:
        print(f"there are {answer:,} unique spelling bees")
    else:
        print(f"{simulation_answer:,} does not match {answer:,}")
