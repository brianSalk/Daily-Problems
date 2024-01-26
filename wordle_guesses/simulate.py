from itertools import product

if __name__ == "__main__":
    ans = set()
    letters = 'qwertyuiopasdfghjklzxcvbnm' # add/subtract characters here to test different values of N
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
        print(len(ans))
    else:
        print(f'got {len(ans)}, expected {equation}')
