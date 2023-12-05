import os
import re


def get_all_number_matches(input_lines):
    return [[(match.group(), match.start(), match.end()) for match in re.finditer(r"[0-9]+", line)] for line in input_lines]


def part1():
    valid_number_sum = 0
    all_number_matches = get_all_number_matches(input_lines)

    for line, number_matches in enumerate(all_number_matches):
        for number_match in number_matches:
            valid = any(
                symbol.start() >= number_match[1] - 1 and symbol.start() <= number_match[2]
                for l in range(-1, 2)
                if 0 <= line + l < len(input_lines)
                for symbol in re.finditer(r"[^\d.]", input_lines[line + l])
            )
            if valid:
                valid_number_sum += int(number_match[0])

    return valid_number_sum


def part2():
    valid_number_sum = 0
    all_symbol_matches = [[match.start() for match in re.finditer(r"[*]", line)] for line in input_lines]

    for line, symbol_matches in enumerate(all_symbol_matches):
        for symbol_match in symbol_matches:
            adj_numbers = [
                int(number_match.group())
                for l in range(-1, 2)
                if 0 <= line + l < len(input_lines)
                for number_match in re.finditer(r"[0-9]+", input_lines[line + l])
                if symbol_match >= number_match.start() - 1 and symbol_match <= number_match.end()
            ]
            if len(adj_numbers) == 2:
                valid_number_sum += adj_numbers[0] * adj_numbers[1]

    return valid_number_sum


def main():
    part1_result = part1()
    print(f"Part 1 answer: {part1_result}")
    part2_result = part2()
    print(f"Part 2 answer: {part2_result}")


if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(directory, 'day3_input.txt')

    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()

    main()
