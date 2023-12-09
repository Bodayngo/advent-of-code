import os
from collections import Counter
from enum import IntEnum


class HandType(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


class Hand:
    def __init__(self, cards, bid, part2=False):
        self.cards = cards
        self.bid = int(bid)
        self.part2 = part2
        self.hand_power = self.get_hand_strength()
        self.card_powers = self.get_card_strengths()

    def get_hand_strength(self):
        card_counts = Counter(self.cards)
        if self.part2 and 'J' in self.cards:
            num_jokers = card_counts.pop('J')
            if not card_counts: return HandType.FIVE_OF_A_KIND
            card_counts[max(card_counts, key=card_counts.get)] += num_jokers
        if len(card_counts) == 1: return HandType.FIVE_OF_A_KIND
        elif len(card_counts) == 2: return HandType.FOUR_OF_A_KIND if 4 in card_counts.values() else HandType.FULL_HOUSE
        elif len(card_counts) == 3: return HandType.THREE_OF_A_KIND if 3 in card_counts.values() else HandType.TWO_PAIRS
        elif len(card_counts) == 4: return HandType.ONE_PAIR
        else: return HandType.HIGH_CARD

    def get_card_strengths(self):
        custom_order = [
            '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'
        ] if not self.part2 else [
            'J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'
        ]
        return [custom_order.index(card) for card in self.cards]
        

def process_input_lines(input_lines, part2):
    return [
        Hand(line.split(' ')[0], int(line.split(' ')[1]), part2)
        for line in input_lines
    ]

def part1(input_lines):
    hands = process_input_lines(input_lines, part2=False)
    hands.sort(key=lambda hand: (hand.hand_power, hand.card_powers))
    return sum([hand.bid * index for index, hand in enumerate(hands, start=1)])

def part2(input_lines):
    hands = process_input_lines(input_lines, part2=True)
    hands.sort(key=lambda hand: (hand.hand_power, hand.card_powers))
    return sum([hand.bid * index for index, hand in enumerate(hands, start=1)])

def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{directory}/puzzle_input.txt"
    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()
    print(f"Part 1 answer: {part1(input_lines)}")
    print(f"Part 2 answer: {part2(input_lines)}")
 
if __name__ == '__main__':
    main()