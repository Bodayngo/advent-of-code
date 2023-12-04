import os
import re

# File input
directory = os.path.dirname(os.path.realpath(__file__))
input_file = f"{directory}/day4_input.txt"
with open(input_file, 'r') as file:
    input_lines = file.read().strip().splitlines()

# Part 1
def part1():
    total_points = []
    for line in input_lines:
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
        total_points.append(points)
    return sum(total_points)

# Part 2
def part2():
    scratchcard_counts = {}
    for index, card in enumerate(input_lines, start=1):
        if index not in scratchcard_counts:
            scratchcard_counts[index] = 1
        else:
            scratchcard_counts[index] += 1

        numbers = re.sub(r'Card\s+\d+:', '', card)
        split_numbers = numbers.split('|')
        winning_numbers = [int(num) for num in split_numbers[0].split()]
        scratched_numbers = [int(num) for num in split_numbers[1].split()]

        matches = 0
        for number in scratched_numbers:
            if number in winning_numbers:
                matches += 1

        if matches != 0:
            for i in range(index+1, index+1+matches):
                scratchcard_counts[i] = scratchcard_counts.get(i, 0) + (1 * scratchcard_counts[index])
    num_cards = 0
    for count in scratchcard_counts.values():
        num_cards += count
    return(num_cards)

def main():
    part1_result = part1()
    print(f"Part 1 answer: {part1_result}")
    part2_result = part2()
    print(f"Part 2 answer: {part2_result}")

if __name__ == '__main__':
    main()