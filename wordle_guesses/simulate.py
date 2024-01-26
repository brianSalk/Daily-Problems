# for this simulation, we cannot use all 26 letters because that would take
# too long to run and would not be practical unless we have a super computer
# so we limit the alphabet to 9 letters and use the equation
# (N-4) * (N-3)^3 - (N-4)^4
# where N is the number of letters in our alphabet

# if we can demonstrate that the equation works with a small N,
# it is likely that it will also work for larger values of N

from itertools import product

if __name__ == "__main__":
    ans = set()
    letters = 'smal56789' # add/subtract characters here to test different values of N
    N = len(letters)
    all_words = (N-4) * (N-3)**3
    no_s = (N-4)**4
    equation = all_words - no_s
    for word in product(letters, repeat=5):
        is_valid = True
        # make sure word does not contain 'm' or 'a'
        if 'm' in word or 'a' in word:
            is_valid = False
        # make sure there is only 1 'l' at position 4 (index 3)
        if word.count('l') >= 2 or word[3] != 'l':
            is_valid = False
        # make sure 's' is not first letter but does appear at least once in the word
        if word[0] == 's' or 's' not in word:
            is_valid = False
        if is_valid:
            ans.add(word)
        
            
    if len(ans) == equation:
        print(len(ans))
    else:
        print(f'got {len(ans)}, expected {equation}')
