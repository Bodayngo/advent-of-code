import os

def parse_lines(input_lines):
    
    for line in input_lines:
        hand
"""
all_freq = {}
for card in hand:
    if card in all_freq:
        all_freq[card] += 1
    else:
        all_freq[card] = 1
"""
def get_hand_type():
    hand = "KTJJT"
    all_freq = {}
    all_freq = {card: all_freq.get(card, 0) + 1 for card in hand}
    print(all_freq)
    res = max(all_freq, key = all_freq.get) 

def part1(input_lines):
    get_hand_type()

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
