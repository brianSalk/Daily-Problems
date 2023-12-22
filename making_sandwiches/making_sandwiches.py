from itertools import combinations_with_replacement
if __name__ == "__main__":
    meats = ["ham", "turkey", "roast beef", "no meat"]
    breads = ["white", "wheat", "rye"]
    cheeses = ["american", "swiss", "cheddar", "provalone", "no cheese"]
    sandwiches = []
    meat_combos = list(combinations_with_replacement(meats, 3))
    bread_combos = list(combinations_with_replacement(breads, 2))
    for bread_combo in bread_combos:
        for meat_combo in meat_combos:
            for cheese in cheeses:
                for lettuce in ["lettuce", "no lettuce"]:
                    sandwiches.append([bread_combo, meat_combo,
                                       cheese, lettuce])
    print(sandwiches)
    print(f'there are {len(sandwiches):,} sandwich combinations')
