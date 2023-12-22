from itertools import permutations

if __name__ == "__main__":
    count = 0
    forbiddens = ["45", "54", "23", "32"]
    for perm in permutations("0123456789"):
        perm = "".join(perm)
        is_valid = True 
        for each in forbiddens:
            if each in perm:
                is_valid = False
                break
        count += is_valid
    print(f'{count:,}')
