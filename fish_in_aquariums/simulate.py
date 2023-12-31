# there are 10 fish, five bass and five bluegill.
# there are 2 aquariums, two round and two cubical.

# The fish are randomly assigned to the aquariums
# how many ways can all the fish be assigned to the aquariums?


# we iterate over all possible combinations of fish
import itertools
from collections import Counter, defaultdict

if __name__ == "__main__":
    fish = ["bass"] * 4 + ["bluegill"] * 4
    ans = set()
    for fish_perms in itertools.permutations(fish):
        for tanks in itertools.combinations_with_replacement(['round', 'cube'], len(fish)):
            fish_tank_counts = [0, 0, 0, 0] #round bass, round bluegill, cube bass, cube bluegill
            for i in range(len(fish)):
                if tanks[i] == 'round' and fish_perms[i] == 'bass':
                    fish_tank_counts[0] += 1
                elif tanks[i] == 'round' and fish_perms[i] == 'bluegill':
                    fish_tank_counts[1] += 1
                elif tanks[i] == 'cube' and fish_perms[i] == 'bass':
                    fish_tank_counts[2] += 1
                elif tanks[i] == 'cube' and fish_perms[i] == 'bluegill':
                    fish_tank_counts[3] += 1
            ans.add(tuple(fish_tank_counts))
    for a in ans:
        print(f'round: {a[0]} bass, {a[1]} bluegill')
        print(f'cube : {a[2]} bass, {a[3]} bluegill')
        print()
    print(len(ans))
