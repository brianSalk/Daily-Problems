# count all 5 digit passwords with 1 or fewer repeated digits
# this enumeration is supposed to be easy to understand,
# not efficient or maintainable
from itertools import permutations

if __name__ == "__main__":
    chars = "11223344556677889900"
    passwords = set()
    for perm in permutations(chars, 5):
        if len(set(perm)) > 3:
            passwords.add("".join(perm))
    print("num perms:", len(passwords))
