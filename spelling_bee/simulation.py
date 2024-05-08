# Created by Brian Salkas

# pick 7 distinct English letters from the 25 letters ('s' is excluded)
# one letter goes in the center, the order of the other letters do not matter
# at least 1 of the selected letters must be a vowel

import math
import itertools

if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrtuvwxyz"
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrtvwxyz'
    simulation_answer = 0
    for middle in alphabet:
        for other_six in itertools.combinations(alphabet, 6):
            if middle in other_six:
                continue
            simulation_answer+=1
            
  
    
    num_letters = len(alphabet)
    num_vowels = len(vowels)
    num_consonants = len(consonants)
    num_outer_letters = 6
    # we must pick at least one vowel, this vowel can be
    # the middle letter or an outer letter
    answer = num_consonants * num_vowels * math.comb(num_letters - 2, num_outer_letters - 1)
    
    if simulation_answer == answer:
        print(f'there are {answer:,} unique spelling bees')
    else:
        print(f'{simulation_answer:,} does not match {answer:,}')
