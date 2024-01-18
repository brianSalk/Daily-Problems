from math import factorial, perm, comb
from itertools import permutations, combinations_with_replacement

def equation(num_customers):
    ans = 0
    for i in range(num_customers + 1):
        ans += factorial(num_customers - i) * factorial(i) * comb(num_customers, i)
    return ans

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
            
    if len(ans) != equation(len(customers)):
        print(f'Equation; {equation(len(customers))}, Simulation: {len(ans)}')
    else:
        print(f'{len(customers)} can form 2 lines {len(ans)} different ways')
