# we are going to use smaller numbers for the simulation
# otherwise it takes too long to run
# this is common in simulations because we want to run them quickly
# we can still varify that the equations are correct by
# plugging in the smaller numbers to the eqations for testing
# and then apply it to the unrestricted real-life problem

# for these problems we will be restricting letters to a through e
# and numbers to 1 through 4

# we will also be reducing the number of letters and numbers per password



from itertools import permutations, combinations_with_replacement, combinations
import math
if __name__ == "__main__":
    # Question a
    # how many passwords can i create with 3 digits, 1 through 4 and 2 lowercase letters, a through e?
    # ans: 5 choose 2 * 4^3 * 5*2 = 16,000
    print('Question a equation 5C2 * 4^3 * 5^2: ')
    passwords = set()
    q1_ans = math.comb(5,2) * 4**3 * 5**2
    for num_com in combinations_with_replacement('1234', 3):
        for let_com in combinations_with_replacement('abcde', 2):
            for perm in permutations(num_com + let_com):
                passwords.add(perm) 
    if q1_ans != len(passwords):
        print(f'expected {q1_ans} passwords, got {len(passwords)}')
    else:
        print(f'question A answer: {q1_ans}')
    
    # Question b
    # how many passwords with 2 digits, 1 through 4 and 3 lowercase letters, a through e and 2 uppercase A through E?
    print('Question b equation: 7! / (2! * 3! * 2!) * 4^2 * 5^3 * 5^2 ')
    passwords = set()
    q2_ans = math.factorial(2+3+2) // (math.factorial(2) * math.factorial(3) * math.factorial(2)) * 4**2 * 5**3 * 5**2
    for num_com in combinations_with_replacement('1234', 2):
        for let_com in combinations_with_replacement('abcde', 3):
            for let_com2 in combinations_with_replacement('ABCDE', 2):
                for perm in permutations(num_com + let_com + let_com2):
                    passwords.add(perm)
    if q2_ans != len(passwords):
        print(f'expected {q2_ans} passwords, got {len(passwords)}')
    else:
        print(f'question B answer: {q2_ans}')

    # Question c 
    # How many passwords starting with 3 digits, 1 through 4 no repeates and ending with 2 upper or lowercase letters a through e?
    passwords = set()
    q3_ans = math.perm(4,3) * 10**2
    print('Question c equation: 4P3 * 10^2')
    for num_perm in permutations('1234', 3):
        for let_com in combinations_with_replacement('abcdeABCDE', 2):
            for let_perm in permutations(let_com):
                passwords.add(num_perm + let_perm)
    if q3_ans != len(passwords):
        print(f'expected {q3_ans} passwords, got {len(passwords)}')
    else:
        print(f'question C answer: {q3_ans}')

"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
