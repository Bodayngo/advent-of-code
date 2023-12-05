import os
import re


def parse_line(line):
    split_line = re.split(': |; |, ', line)
    game_number = int(split_line.pop(0).split(' ')[1])
    dice_counts_tuples = [(int(item.split()[0]), item.split()[1]) for item in split_line]
    dice_counts_tuples.sort(reverse=True)

    return game_number, dice_counts_tuples


def part1():
    limits = {'red': 12, 'green': 13, 'blue': 14,}
    passed_games = [
        game_number
        for game_number, counts in (parse_line(line) for line in input_lines)
        if all(
            count[0] <= limits[count[1]]
            for count in counts
        )
    ]

    return sum(passed_games)


def part2():
    powers = []
    for _, counts in (parse_line(line) for line in input_lines):
        highest_red = next((t for t in counts if 'red' in t), None)[0]
        highest_green = next((t for t in counts if 'green' in t), None)[0]
        highest_blue = next((t for t in counts if 'blue' in t), None)[0]
        power = highest_red * highest_green * highest_blue
        powers.append(int(power))

    return sum(powers)


def main():
    part1_result = part1()
    print(f"Part 1 answer: {part1_result}")
    part2_result = part2()
    print(f"Part 2 answer: {part2_result}")


if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(directory, 'day2_input.txt')

    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()

    main()
