import os
import re
from collections import defaultdict

def process_line(line):
    numbers = re.sub(r'Card\s+\d+:', '', line)
    split_numbers = numbers.split('|')
    winning_numbers = [int(num) for num in split_numbers[0].split()]
    scratched_numbers = [int(num) for num in split_numbers[1].split()]

    points = 0
    for number in scratched_numbers:
        if number in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    return winning_numbers, scratched_numbers

def part1():
    return sum(1 for _, scratched_numbers in (process_line(line) for line in input_lines) if any(num in scratched_numbers for num in _))

def part2():
    scratchcard_counts = defaultdict(int)
    for index, card in enumerate(input_lines, start=1):
        scratchcard_counts[index] += 1

        winning_numbers, scratched_numbers = process_line(card)

        matches = sum(1 for number in scratched_numbers if number in winning_numbers)
        for i in range(index + 1, index + 1 + matches):
            scratchcard_counts[i] += 1 * scratchcard_counts[index]

    return sum(scratchcard_counts.values())

def main():
    part1_result = part1()
    print(f"Part 1 answer: {part1_result}")
    part2_result = part2()
    print(f"Part 2 answer: {part2_result}")

if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(directory, 'day4_input.txt')

    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()

    main()
