# count the number of words 2 to 3 letter permutations 
# that can be created from the word hello
# ---------- simulation -----------------------------------------
# we can simulate this by using the permutations function from itertools
# permutations takes a word (w) and a length (l) and returns a set of permutations
# of length l of the word w
# we store the results in a set to remove duplicates
# we can use the set union operator |= to add the results of each call to the set
# we can use the len function to count the number of elements in the set
# we perform the above for l=2 and l=3, then add the results int the same set
# ----------------- math -----------------------------------
# count the number of 2 or 3 unique letter permutations from the word hello
# let's start with 2
# this means we are selecting l letters from the set {h, e, l, o} if w=hello
# this gives us len(set(w)) permute l (12 if l=2 and w=hello)
# then count the number of unique permutations with 2 l's (just 1 in our case)
# now do the same for l=3
# this gives us len(set(w)) permutation l (24 if l=3 and w=hello)
# then we count the number of unique permutations with 2 l's and 1 of {h, e, o}
#   there are three places to put extra character xll, lxl, llx
#   there are 3 unique characters to choose from, leaving us with 3*3=9 unique permutations
# now we add that all up: 12 + 1 + 24 + 9 = 46

# ------------------ simulation code -------------------------------
from itertools import permutations


def simulate(word):
    word_set = set()
    for i in range(2, 4):
        word_set |= set(permutations(word, i))
    print(word_set)
    print(f'there are {len(word_set)} unique 2 or 3 letter permutations of {word}')


if __name__ == "__main__":
    print("part 1: count 2 and 3 letter permutations of hello where l's are indistinguishable")
    word = "hello"
    simulate(word)
    print("part 2: count 2 and 3 letter permutations of hello where l's are distinguishable")
    word = "helLo"
    simulate(word)
"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
