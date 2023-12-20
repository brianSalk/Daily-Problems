from itertools import permutations

if __name__ == "__main__":
    chars = "11223344556677889900"
    passwords = set()
    for perm in permutations(chars, 5):
        if len(set(perm)) > 3:
            passwords.add("".join(perm))
        else:
            #print("".join(perm))
            ...
    print("num perms:", len(passwords))
