# count 3 digit numbers with all ascending digits
# count 4 digit numbers with all ascending digits
from itertools import permutations, combinations_with_replacement
def is_increase(s):
    for i in range(len(s)-1):
        if s[i+1] <= s[i]:
            return False
    return True
if __name__ == "__main__":
    count3 = count4 = 0
    for num in range(10_000):
        count3 += (999 >= num >= 100) and is_increase(str(num))
        count4 += (9_999 >= num >= 1_000) and is_increase(str(num))
    print(f'3 digit numbers with all ascending digits: {count3}')
    print(f'4 digit numbers with all ascending digits: {count4}')
