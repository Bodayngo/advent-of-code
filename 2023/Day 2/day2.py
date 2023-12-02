import os
import re

directory = os.path.dirname(os.path.realpath(__file__))
input_file = f"{directory}/day2_input.txt"


def part1():
    with open(input_file, 'r') as f:
        passed_games = []
        for line in f.read().splitlines():
            split_line = re.split(': |; |, ', line)
            game_number = split_line.pop(0).split(' ')[1]
            passed_game = True
            for i in split_line:
                if 'red' in i and int(i.split(' ')[0]) > 12:
                    passed_game = False
                elif 'green' in i and int(i.split(' ')[0]) > 13:
                    passed_game = False
                elif 'blue' in i and int(i.split(' ')[0]) > 14:
                    passed_game = False
            if passed_game == True:
                passed_games.append(int(game_number))
        return sum(passed_games)
    

def part2():
    with open(input_file, 'r') as f:
        powers = []
        for line in f.read().splitlines():
            dice_counts = re.split(': |; |, ', line)
            dice_counts.pop(0)
            dice_counts_tuples = [(int(item.split()[0]), item.split()[1]) for item in dice_counts]
            dice_counts_tuples.sort(reverse=True)
            highest_red = next((t for t in dice_counts_tuples if 'red' in t), None)[0]
            highest_green = next((t for t in dice_counts_tuples if 'green' in t), None)[0]
            highest_blue = next((t for t in dice_counts_tuples if 'blue' in t), None)[0]
            power = highest_red * highest_green * highest_blue
            powers.append(int(power))
        return sum(powers)



def main():
    part1_result = part1()
    print(f"Part 1 answer: {part1_result}")
    part2_result = part2()
    print(f"Part 2 answer: {part2_result}")


if __name__ == '__main__':
    main()