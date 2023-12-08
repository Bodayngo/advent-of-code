import os
from collections import Counter


class Hand:
    def __init__(self, hand: str, bid: str):
        self.cards = hand
        self.bid = int(bid)
        self.counts = Counter(hand)
        self.num_jokers = hand.count('J')
        self.hand_power_1 = self.get_hand_power_1()
        self.card_powers_1 = self.get_card_powers_1()
        self.hand_power_2 = self.get_hand_power_2()
        self.card_powers_2 = self.get_card_powers_2()

    def get_hand_power_1(self) -> int:
        """
        7: Five of a kind
        6: Four of a kind
        5: Full house
        4: Three of a kind
        3: Two pair
        2: One pair
        1: High card
        """
        card_counts = list(self.counts.values())
        card_counts.sort(reverse=True)
        if card_counts[0] == 5: return 7
        elif card_counts[0] == 4: return 6
        elif card_counts[0] == 3:
            if card_counts[1] == 2: return 5
            else: return 4
        elif card_counts[0] == 2:
            if card_counts.count(2) == 2: return 3
            else: return 2
        else: return 1
    
    def get_card_powers_1(self):
        card_powers = []
        custom_order = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
        for card in self.cards:
            card_powers.append(custom_order[card])
        return card_powers
    
    def get_hand_power_2(self) -> int:
        """
        7: Five of a kind
        6: Four of a kind
        5: Full house
        4: Three of a kind
        3: Two pair
        2: One pair
        1: High card
        """
        card_counts = list(self.counts.values())
        card_counts.sort(reverse=True)
        if card_counts[0] == 5: return 7
        elif card_counts[0] == 4:
            return 7 if self.num_jokers in [1, 4] else 6
        elif card_counts[0] == 3:
            if self.num_jokers == 2 or (self.num_jokers == 3 and card_counts[1] == 2): return 7
            elif self.num_jokers in [1, 3]: return 6
            elif card_counts[1] == 2: return 5
            else: return 4
        elif card_counts[0] == 2:
            if card_counts.count(2) == 2 and self.num_jokers == 2: return 6
            elif card_counts.count(2) == 2 and self.num_jokers == 1: return 5
            elif self.num_jokers == 1: return 4
            elif card_counts.count(2) == 2: return 3
            else: return 2
        else: return 2 if self.num_jokers == 1 else 1
    
    def get_card_powers_2(self):
        card_powers = []
        custom_order = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
        for card in self.cards:
            card_powers.append(custom_order[card])
        return card_powers


def part1(hands):
    hands.sort(key=lambda hand: (hand.hand_power_1, hand.card_powers_1))
    return sum([hand.bid * index for index, hand in enumerate(hands, start=1)])


def part2(hands):
    hands.sort(key=lambda hand: (hand.hand_power_2, hand.card_powers_2))
    for hand in hands:
        print(hand.cards)
        print(hand.hand_power_2)
    return sum([hand.bid * index for index, hand in enumerate(hands, start=1)])


def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{directory}/test_input.txt"
    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()
    hands = [
        Hand(line.split(' ')[0], line.split(' ')[1])
        for line in input_lines
    ]
    print(f"Part 1 answer: {part1(hands)}")
    print(f"Part 2 answer: {part2(hands)}")
 

if __name__ == '__main__':
    main()