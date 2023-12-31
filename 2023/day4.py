import os
import re
from collections import defaultdict

def process_line(line):
    numbers = re.sub(r'Card\s+\d+:', '', line)
    split_numbers = numbers.split('|')
    winning_numbers = [int(num) for num in split_numbers[0].split()]
    scratched_numbers = [int(num) for num in split_numbers[1].split()]
    return winning_numbers, scratched_numbers

def part1(input_lines):
    total_points = 0
    for card in input_lines:
        winning_numbers, scratched_numbers = process_line(card)
        points = 0
        for number in scratched_numbers:
            if number in winning_numbers:
                points = 1 if points == 0 else points * 2
        total_points += points
    return total_points

def part2(input_lines):
    scratchcard_counts = defaultdict(int)
    for index, card in enumerate(input_lines, start=1):
        scratchcard_counts[index] += 1
        winning_numbers, scratched_numbers = process_line(card)
        matches = sum(1 for number in scratched_numbers if number in winning_numbers)
        for i in range(index + 1, index + 1 + matches):
            scratchcard_counts[i] += 1 * scratchcard_counts[index]
    return sum(scratchcard_counts.values())

def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{directory}/day4_input.txt"
    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()
    print(f"Part 1 answer: {part1(input_lines)}")
    print(f"Part 2 answer: {part2(input_lines)}")

if __name__ == '__main__':
    main()
