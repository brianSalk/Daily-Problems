import math
import itertools
    
    
def multinomial(n, group_sizes):
    denominator = 1
    for group_size in group_sizes:
        denominator *= math.factorial(group_size)
    return math.factorial(n) // denominator
    
    
if __name__ == "__main__":
    colors = 'rrrrgggyy'
    simulation_answer = len(set(itertools.permutations(colors)))
    color_counts = [colors.count('r'), colors.count('g'), colors.count('y')]
    answer = multinomial(len(colors), color_counts)
    if simulation_answer == answer:
        print(f'There are {answer:,} ways for the different colored shirts to be arranged')
    else:
        print(f'{answer} does not match {simulation_answer}')
