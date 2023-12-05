# Import necessary module(s)
import os
import re

# Function to parse a line of input and extract relevant information
def parse_line(line):
    # Split the line using specified delimiters and create a list
    split_line = re.split(': |; |, ', line)
    # Extract game number and remove it from the list
    game_number = int(split_line.pop(0).split(' ')[1])
    # Create a list of tuples containing dice counts and colors, then sort in descending order by count
    dice_counts_tuples = [(int(item.split()[0]), item.split()[1]) for item in split_line]
    dice_counts_tuples.sort(reverse=True)
    # Return game number and sorted dice counts
    return game_number, dice_counts_tuples

# Function for Part 1
def part1():
    # Define limits for each color
    limits = {'red': 12, 'green': 13, 'blue': 14}
    # Extract game numbers for games that meet specified conditions
    passed_games = [
        game_number
        for game_number, counts in (parse_line(line) for line in input_lines)
        if all(
            count[0] <= limits[count[1]]
            for count in counts
        )
    ]
    # Return the sum of passed game numbers
    return sum(passed_games)

# Function for Part 2
def part2():
    # List to store powers calculated for each game
    powers = []
    # Calculate power for each game and add it to the powers list
    for _, counts in (parse_line(line) for line in input_lines):
        highest_red = next((t for t in counts if 'red' in t), None)[0]
        highest_green = next((t for t in counts if 'green' in t), None)[0]
        highest_blue = next((t for t in counts if 'blue' in t), None)[0]
        power = highest_red * highest_green * highest_blue
        powers.append(int(power))
    # Return the sum of all calculated powers
    return sum(powers)

# Main function to execute the program
def main():
    # Calculate and print Part 1 result
    part1_result = part1()
    print(f"Part 1 answer: {part1_result}")
    # Calculate and print Part 2 result
    part2_result = part2()
    print(f"Part 2 answer: {part2_result}")

# Entry point of the script
if __name__ == '__main__':
    # Get the directory of the script and construct the input file path
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(directory, 'day2_input.txt')

    # Read input lines from the file and strip whitespace
    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()

    # Call the main function to run the program
    main()
