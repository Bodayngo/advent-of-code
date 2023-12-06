import os

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

def part1(input_lines):
    number_list = []
    for line in input_lines:
        numbers = ''.join(c for c in line if c.isdigit())
        number_list.append(int(f"{numbers[:1]}{numbers[-1:]}"))
    return sum(number_list)

def part2(input_lines):
    numbers = []
    for line in input_lines:
        found_numbers = []
        for alpha, num in alpha_num_mappings.items():
            index = line.find(num)
            if index != -1:
                found_numbers.append((index, num))
            index = line.find(alpha)
            if index != -1:
                found_numbers.append((index, num))
            index = line.rfind(num)
            if index != -1:
                found_numbers.append((index, num))
            index = line.rfind(alpha)
            if index != -1:
                found_numbers.append((index, num))
        found_numbers.sort()
        number = f"{found_numbers[0][1]}{found_numbers[-1][1]}"
        numbers.append(int(number))
    return sum(numbers)

def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(directory, 'day1_input.txt')
    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()
    print(f"Part 1 answer: {part1(input_lines)}")
    print(f"Part 2 answer: {part2(input_lines)}")

if __name__ == "__main__":

    main()
