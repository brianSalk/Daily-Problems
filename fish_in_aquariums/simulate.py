# there are 10 fish, five bass and five bluegill.
# there are 2 aquariums, two round and two cubical.

# The fish are randomly assigned to the aquariums
# how many ways can all the fish be assigned to the aquariums?
import itertools
from collections import Counter, defaultdict
if __name__ == '__main__':
    import itertools
    fish = ['bass'] * 5 + ['bluegill'] * 5
    aquariums = ['round', 'cubical']
    ans = set()
    for fish_perm in itertools.permutations(fish):
        arrangement = {'round': defaultdict(int),'cube': defaultdict(int)}
        for aquarium_index in itertools.combinations_with_replacement(['round', 'cube'], 10):
            for i in range(10):
                arrangement[aquarium_index[i]][fish_perm[i]] += 1
            round_dict = frozendict(arrangement['round'])
    print('There are {} unique combinations'.format(len(unique_combinations)))
    for c in unique_combinations:
        print(c)
