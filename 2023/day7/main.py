import os
from collections import Counter


def get_hand_ranking(hand):
    """
    1: Five of a kind
    2: Four of a kind
    3: Full house
    4: Three of a kind
    5: Two pair
    6: One pair
    7: High card
    """
    card_counts = Counter(hand)
    max_occurrence = max(card_counts.values())
    #ranking_dict = {5: 1, 4: 2, 3: 3 if hand[0] == hand[-1] and len(set(hand[1:4])) == 1 else 4, 2: 5 if list(card_counts.values()).count(2) == 2 else 6}
    #return ranking_dict.get(max_occurrence, 7)
    if max_occurrence == 5:
        return 1 # Five of a kind
    elif max_occurrence == 4:
        return 2 # Four of a kind
    elif max_occurrence == 3:
        if hand[0] == hand[-1] and len(set(hand[1:4])) == 1:
            return 3 # Full house
        else:
            return 4 # Three of a kind
    elif max_occurrence == 2:
        if list(card_counts.values()).count(2) == 2:
            return 5 # Two pair
        else:
            return 6 # One pair
    else:
        return 7 # High card

def custom_order(character):
    custom_order = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
    return custom_order.get(character)

def custom_sort(item):
    custom_order = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
    return [custom_order.get(character) for character in item[0]]

def calculate_bid_rank_products(sorted_bid_list):
    return [int(bid) * (index + 1) for index, bid in enumerate(sorted_bid_list)]

def part1(input_lines):
    hand_rankings_by_type = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for line in input_lines:
        hand, bid = line.split(' ')[:2]
        hand_rankings_by_type[get_hand_ranking(hand)].append((hand, bid))
    for hand_type in hand_rankings_by_type.keys():
        hand_rankings_by_type[hand_type] = sorted(hand_rankings_by_type[hand_type], key=custom_sort)
        print(hand_type)
        for hand in hand_rankings_by_type[hand_type]:
            print(hand)
    sorted_bid_list = [
        value[1] 
        for values in hand_rankings_by_type.values() 
        for value in values
    ]
    sorted_bid_list.reverse()
    bid_rank_products = calculate_bid_rank_products(sorted_bid_list)
    return sum(bid_rank_products)


def part2(input_lines):
    pass


def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{directory}/test_input.txt"
    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()
    print(f"Part 1 answer: {part1(input_lines)}")
    print(f"Part 2 answer: {part2(input_lines)}")
 

if __name__ == '__main__':
    main()
