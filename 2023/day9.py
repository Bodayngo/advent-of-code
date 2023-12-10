import os
import operator

def parse_input(input_lines):
    return [
        [int(number) for number in line.split(' ')]
        for line in input_lines
        ]

def derive_missing_number(numbers: list[int], part2: bool=False):
    outer_numbers = [numbers[0] if part2 else numbers [-1]]
    while True:
        numbers = list(map(operator.sub, numbers[1:], numbers[:-1]))
        if len(set(numbers)) == 1:
            lowest_diff = numbers[0]
            break
        outer_numbers.append(numbers[0] if part2 else numbers[-1])
    if not part2:
        return sum(outer_numbers) + lowest_diff
    else:
        result = lowest_diff
        for number in reversed(outer_numbers):
            result = number - result
        return result

def part1(numbers_list):
    derived_last_numbers = [derive_missing_number(numbers) for numbers in numbers_list]
    return sum(derived_last_numbers)

def part2(numbers_list):
    derived_first_numbers = [derive_missing_number(numbers, part2=True) for numbers in numbers_list]
    return sum(derived_first_numbers)

def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{directory}/puzzle_input.txt"
    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()
    numbers_lists = parse_input(input_lines)
    print(f"Part 1 answer: {part1(numbers_lists)}")
    print(f"Part 2 answer: {part2(numbers_lists)}")
 
if __name__ == '__main__':
    main()
