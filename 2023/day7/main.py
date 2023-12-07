import os
from collections import Counter


def get_hand_ranking(hand):
    card_counts = Counter(hand)
    max_occurrence = max(card_counts.values())
    ranking_dict = {5: 1, 4: 2, 3: 3 if hand[0] == hand[-1] else 4, 2: 5 if list(card_counts.values()).count(2) == 2 else 6}
    return ranking_dict.get(max_occurrence, 7)

def custom_order(character):
    order = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
    return order.get(character)

def custom_sort(item):
    return [custom_order(char) for char in item[0]]

def calculate_bid_rank_products(sorted_bid_list):
    return [int(bid) * (index + 1) for index, bid in enumerate(sorted_bid_list)]

def part1(input_lines):
    hand_rankings_by_type = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for line in input_lines:
        hand, bid = line.split(' ')[:2]
        hand_rankings_by_type[get_hand_ranking(hand)].append((hand, bid))
    print(hand_rankings_by_type)
    for type_ranking in hand_rankings_by_type.keys():
        hand_rankings_by_type[type_ranking] = sorted(hand_rankings_by_type[type_ranking], key=custom_sort)
    for key, value in hand_rankings_by_type.items():
        print(key)
        for i in value:
            print(i)
    sorted_bid_list = [value[1] for values in hand_rankings_by_type.values() for value in values]
    print(sorted_bid_list)
    sorted_bid_list.reverse()
    print(sorted_bid_list)
    for index, hand in enumerate(sorted_bid_list):
        rank = index + 1
        print(rank)
        print(int(hand))
    bid_rank_products = calculate_bid_rank_products(sorted_bid_list)
    return sum(bid_rank_products)


def part2(input_lines):
    pass


def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{directory}/puzzle_input.txt"

    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()

    print(f"Part 1 answer: {part1(input_lines)}")
    print(f"Part 2 answer: {part2(input_lines)}")
 

if __name__ == '__main__':
    main()
