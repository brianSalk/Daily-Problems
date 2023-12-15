# count the number of words 2 to 3 letter permutations 
# that can be created from the word hello
from itertools import permutations

if __name__ == "__main__":
    word = "hello"
    word_set = set()
    for i in range(2, 4):
        word_set |= set(permutations(word, i))
    print(word_set)
    print(f'there are {len(word_set)} unique 2 or 3 letter permutations of {word}')
