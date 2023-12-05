# Import necessary module(s)
import os

# Function for Part 1
def part1():
    # List to store extracted numbers
    number_list = []
    # Iterate over each line in the input and extract numbers
    for line in input_lines:
        # Extract digits from the line and concatenate the first and last digit
        numbers = ''.join(c for c in line if c.isdigit())
        number_list.append(int(f"{numbers[:1]}{numbers[-1:]}"))
    # Return the sum of extracted numbers
    return sum(number_list)

# Dictionary mapping words to their corresponding numerical representations
alpha_num_mappings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# Function for Part 2
def part2():
    # List to store extracted numbers
    numbers = []
    # Iterate over each line in the input
    for line in input_lines:
        # List to store found numbers and their indices
        found_numbers = []
        # Iterate over each entry in the alpha_num_mappings dictionary
        for alpha, num in alpha_num_mappings.items():
            # Find the index of the numerical representation in the line
            index = line.find(num)
            if index != -1:
                found_numbers.append((index, num))
            # Find the index of the word representation in the line
            index = line.find(alpha)
            if index != -1:
                found_numbers.append((index, num))
            # Find the rightmost index of the numerical representation in the line
            index = line.rfind(num)
            if index != -1:
                found_numbers.append((index, num))
            # Find the rightmost index of the word representation in the line
            index = line.rfind(alpha)
            if index != -1:
                found_numbers.append((index, num))

        # Sort the found numbers based on their indices
        found_numbers.sort()
        # Construct the number by concatenating the first and last found numbers
        number = f"{found_numbers[0][1]}{found_numbers[-1][1]}"
        numbers.append(int(number))

    # Return the sum of extracted numbers
    return sum(numbers)

# Main function to execute the program
def main():
    # Calculate and print Part 1 result
    part1_result = part1()
    print(f"Part 1 answer: {part1_result}")
    # Calculate and print Part 2 result
    part2_result = part2()
    print(f"Part 2 answer: {part2_result}")

# Entry point of the script
if __name__ == "__main__":
    # Get the directory of the script and construct the input file path
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(directory, 'day1_input.txt')

    # Read input lines from the file and strip whitespace
    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()

    # Call the main function to run the program
    main()
