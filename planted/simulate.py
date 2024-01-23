import itertools
import math
if __name__ == "__main__":
    ans = 0
    equation = math.comb(7, 4) - 1
    for i in range(1,5):
        s = set()
        for comb in itertools.combinations('AAAABBBBCCCC', i):
            s.add(comb)
        ans += len(s)
    print(f'Expected {equation}, got {ans}')
