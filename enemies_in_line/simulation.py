from math import comb, factorial, perm
from itertools import permutations

def has_forbidden_neighbors(l):
    prev = ""
    for each in l:
        if each == prev == "|":
            return True
        prev = each
    return False

if __name__ == "__main__":
    l = "||||******"
    
    k = l.count('|')
    n = len(l)
    
    ans = 0
    eq = comb((n-k)+1, k) * factorial(k) * factorial(n-k)
    for perm in permutations(l):
        ans += not has_forbidden_neighbors(perm)
    
    if ans == eq:
        print(ans)
    else:
        print(f'{ans} does not equal {eq}')
        
"""
created by brian salkas
"""
