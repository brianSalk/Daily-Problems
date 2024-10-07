import itertools
people = ['Earthling Ed', 'Joey Carbstrong', 'Humane Hancock', 'Peter Singer', 'Gary Yourofsky', 'Melanie Joy']

one_line_permutations = set(list(itertools.permutations(people)))
two_line_permutations = set(list(itertools.permutations(people))) # only differ by spacial location, no need to test differently
permutations_of_five = set(list(itertools.permutations(people, r=5)))
if not 720 == len(one_line_permutations) == len(two_line_permutations) == len(permutations_of_five):
    print('They should all be the same')
    exit()
print('All permutations are equal to 720')