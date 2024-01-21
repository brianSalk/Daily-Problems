from itertools import combinations
from math import comb
from collections import Counter
class Card:
    def __init__(self, suite: str, rank: str):
        self.suite = suite.title()
        self.rank = rank.upper()

    def __repr__(self):
        return f'{self.rank}: {self.suite}'

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suite < other.suite
        return self.rank < other.rank
    

class Deck:
    def __init__(self):
        self.cards = []
        for suite in ['Spades', 'Clubs', 'Hearts', 'Diamonds']:
            for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(suite=suite, rank=rank))


if __name__ == "__main__":
    deck = Deck()
    one_pair = comb(4, 2) * comb(13, 1) * comb(4, 1)**3 * comb(12, 3)
    two_pair = comb(4, 2)**2 * comb(13, 2) * comb(4, 1) * comb(11, 1)
    three_of_a_kind = comb(4, 3) * comb(13, 1) * comb(4, 1)**2 * comb(12, 2)
    four_of_a_kind = comb(4, 4) * comb(13, 1) * comb(4, 1) * comb(12, 1)
    one_pair_count = set()
    two_pair_count = set()
    three_of_a_kind_count = set()
    four_of_a_kind_count = set()
    for com in combinations(deck.cards, 5):
        ranks = set()
        suites = set()
        for card in com:
            ranks.add(card.rank)
        if len(ranks) == 4:
            one_pair_count.add(com)
        if len(ranks) == 3 and 2 in Counter([each.rank for each in com]).values():
            two_pair_count.add(com)
        if len(ranks) == 3 and 3 in Counter([each.rank for each in com]).values():
            three_of_a_kind_count.add(com)
        if len(ranks) == 2 and 4 in Counter([each.rank for each in com]).values():
            four_of_a_kind_count.add(com)

    if len(one_pair_count) != one_pair:
        print(f'Something went wrong: Expected {one_pair} but got {len(one_pair_count)}')
    else:
        print(f'A) {one_pair}')

    if len(two_pair_count) != two_pair:
        print(f'Something went wrong: Expected {two_pair} but got {len(two_pair_count)}')
    else:
        print(f'B) {two_pair}')

    if len(three_of_a_kind_count) != three_of_a_kind:
        print(f'Something went wrong: Expected {three_of_a_kind} but got {len(three_of_a_kind_count)}')
    else:
        print(f'C) {three_of_a_kind}')

    if len(four_of_a_kind_count) != four_of_a_kind:
        print(f'Something went wrong: Expected {four_of_a_kind} but got {len(four_of_a_kind_count)}')
    else:
        print(f'D) {four_of_a_kind}')
