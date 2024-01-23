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
    straight_count, full_house_count, flush_count = [set() for _ in range(3)]
    straight_flush = 10 * 4
    flush = 4 * comb(13, 5) - straight_flush
    straight = 10 * 4**5 - straight_flush
    full_house = 13 * comb(4, 3) * 12 * comb(4, 2)
    
    for hand in combinations(deck.cards, 5):
        suits = set()
        ranks = Counter()
        for card in hand:
            suits.add(card.suite)
            ranks.update([card.rank])
            
        sorted_hand = sorted(hand)
        is_straight = True
        
        for i, each in enumerate(sorted_hand):
            each= each.rank
            if each in ['2','3','4','5','6','7','8','9','10']:
                sorted_hand[i] = int(each)
            elif each == "J":
                sorted_hand[i] = 11
            elif each == "Q":
                sorted_hand[i] = 12
            elif each == "K":
                sorted_hand[i] = 13
            elif each == "A":
                sorted_hand[i] = 1
            
        sorted_hand = sorted(sorted_hand)
        if 1 not in sorted_hand:
            for i, each in enumerate(sorted_hand[1:]):
                i+=1
                if sorted_hand[i-1] + 1 != sorted_hand[i]:
                    is_straight = False
                    break
        else:
            # we need to do this because Ace can be high or low
            is_straight1=is_straight2 = True
            for i, each in enumerate(sorted_hand[1:]):
                i+=1
                if sorted_hand[i-1] + 1 != sorted_hand[i]:
                    is_straight1 = False
                    break
            sorted_hand.pop(0)
            sorted_hand.append(14)
            for i, each in enumerate(sorted_hand[1:]):
                i+=1
                if sorted_hand[i-1] + 1 != sorted_hand[i]:
                    is_straight2 = False
                    break
            is_straight = max(is_straight1, is_straight2)
            
                
            
        if len(suits) == 1 and not is_straight:
            flush_count.add(hand)
        if is_straight and len(suits) != 1:
            straight_count.add(hand)
        if 2 in ranks.values() and 3 in ranks.values():
            full_house_count.add(hand)
    print(f'Expected: {len(flush_count)}, Got: {flush}')
    print(f'Expected: {len(straight_count)}, Got: {straight}')
    print(f'Expected: {len(full_house_count)}, Got: {full_house}')
    
