# how many breakfasts can i create if i must choose:
# one or fewer entree:
#    pancakes
#    waffles
#    french toast

# one or fewer drinks:
#    coffee
#    tea
#    orange juice
#    milk

# one or fewer sides:
#    breakfast sausage
#    fruit

if __name__ == '__main__':
    entrees = ['pancakes', 'waffles', 'french toast']
    drinks = ['coffee', 'tea', 'orange juice', 'milk']
    sides = ['breakfast sausage', 'fruit']

    breakfasts = 0
    for entree in entrees:
        for drink in drinks:
            for side in sides:
                print(entree, drink, side)
                breakfasts += 1

    print(f'there are {breakfasts} breakfasts')

"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
