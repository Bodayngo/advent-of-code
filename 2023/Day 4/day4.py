# Import necessary module(s)
import os
import re
from collections import defaultdict

# Function to process a line and extract winning and scratched numbers
def process_line(line):
    # Remove card number and split the line into winning and scratched numbers
    numbers = re.sub(r'Card\s+\d+:', '', line)
    split_numbers = numbers.split('|')
    winning_numbers = [int(num) for num in split_numbers[0].split()]
    scratched_numbers = [int(num) for num in split_numbers[1].split()]

    # Calculate points based on scratched and winning numbers
    points = 0
    for number in scratched_numbers:
        if number in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    return winning_numbers, scratched_numbers

# Function for Part 1
def part1():
    # Initialize total points
    total_points = 0
    # Iterate over each card in the input
    for card in input_lines:
        # Process the line to get winning and scratched numbers
        winning_numbers, scratched_numbers = process_line(card)

        # Calculate points for each scratched number
        points = 0
        for number in scratched_numbers:
            if number in winning_numbers:
                points = 1 if points == 0 else points * 2
        # Add points to the total
        total_points += points

    # Return the total points
    return total_points

# Function for Part 2
def part2():
    # Use a defaultdict to count the number of times a scratchcard is used
    scratchcard_counts = defaultdict(int)
    # Iterate over each card in the input with an index
    for index, card in enumerate(input_lines, start=1):
        # Increment the count for the current scratchcard
        scratchcard_counts[index] += 1

        # Process the line to get winning and scratched numbers
        winning_numbers, scratched_numbers = process_line(card)

        # Count the number of matches and update counts for subsequent scratchcards
        matches = sum(1 for number in scratched_numbers if number in winning_numbers)
        for i in range(index + 1, index + 1 + matches):
            scratchcard_counts[i] += 1 * scratchcard_counts[index]

    # Return the sum of scratchcard counts
    return sum(scratchcard_counts.values())

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
    input_file = os.path.join(directory, 'day4_input.txt')

    # Read input lines from the file and strip whitespace
    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()

    # Call the main function to run the program
    main()
