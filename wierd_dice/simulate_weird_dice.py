import random
from itertools import combinations, combinations_with_replacement

class Die:
    def __init__(self, values):
        self.sides = len(values)
        self.values = values

    def roll(self):
        return random.choice(self.values)


if __name__ == "__main__":
    letters = ["A", "B", "C"]
    numbers = [1, 2, 3, 4]
    roman_numerals = ["I", "II", "III", "IV", "V"]
    emojies = ["🔥", "💩", "👻", "😍", "😡", "😱"]
    countries = ["KR", "JP", "DE", "MG", "CN", "DK", "UA"]
    letters_die = Die(letters)
    numbers_die = Die(numbers)
    roman_numerals_die = Die(roman_numerals)
    emojies_die = Die(emojies)
    countries_die = Die(countries)
    dice = [letters_die, numbers_die, roman_numerals_die, emojies_die, countries_die]
    num_trials = 100_000_000
    for _ in range(num_trials):
        chosen_dice = random.choices(dice, k=3)

