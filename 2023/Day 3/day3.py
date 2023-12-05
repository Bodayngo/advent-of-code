# Import necessary module(s)
import os
import re

# Function to extract all number matches in each line
def get_all_number_matches(input_lines):
    # Use regular expression to find all number matches in each line
    return [[(match.group(), match.start(), match.end()) for match in re.finditer(r"[0-9]+", line)] for line in input_lines]

# Function for Part 1
def part1():
    # Initialize the sum of valid numbers
    valid_number_sum = 0
    # Get all number matches in each line
    all_number_matches = get_all_number_matches(input_lines)

    # Iterate over each line and its number matches
    for line, number_matches in enumerate(all_number_matches):
        # Iterate over each number match in the line
        for number_match in number_matches:
            # Check if the number is valid based on surrounding symbols
            valid = any(
                symbol.start() >= number_match[1] - 1 and symbol.start() <= number_match[2]
                for l in range(-1, 2)
                if 0 <= line + l < len(input_lines)
                for symbol in re.finditer(r"[^\d.]", input_lines[line + l])
            )
            # If valid, add the number to the sum
            if valid:
                valid_number_sum += int(number_match[0])

    # Return the sum of valid numbers
    return valid_number_sum

# Function for Part 2
def part2():
    # Initialize the sum of valid numbers
    valid_number_sum = 0
    # Get all symbol matches for each line
    all_symbol_matches = [[match.start() for match in re.finditer(r"[*]", line)] for line in input_lines]

    # Iterate over each line and its symbol matches
    for line, symbol_matches in enumerate(all_symbol_matches):
        # Iterate over each symbol match in the line
        for symbol_match in symbol_matches:
            # Find adjacent numbers based on the symbol's position
            adj_numbers = [
                int(number_match.group())
                for l in range(-1, 2)
                if 0 <= line + l < len(input_lines)
                for number_match in re.finditer(r"[0-9]+", input_lines[line + l])
                if symbol_match >= number_match.start() - 1 and symbol_match <= number_match.end()
            ]
            # If there are two adjacent numbers, add their product to the sum
            if len(adj_numbers) == 2:
                valid_number_sum += adj_numbers[0] * adj_numbers[1]

    # Return the sum of valid numbers
    return valid_number_sum

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
    input_file = os.path.join(directory, 'day3_input.txt')

    # Read input lines from the file and strip whitespace
    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()

    # Call the main function to run the program
    main()
