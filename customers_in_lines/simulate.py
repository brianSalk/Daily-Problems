from math import factorial, perm, comb
from itertools import permutations, combinations_with_replacement


if __name__ == "__main__":
    customers = "ABCDE"
    ans = set()
    for customer_permutation in permutations(customers):
        registers = [[],[]]
        for register_indexes in combinations_with_replacement([0,1], 5):
            for i, register_index in enumerate(register_indexes):
                registers[register_index].append(customer_permutation[i])
            a, b = registers
            ans.add((tuple(a),tuple(b)))
            
    print(len(ans))
