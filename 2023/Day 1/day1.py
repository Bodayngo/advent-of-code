import os

directory = os.path.dirname(os.path.realpath(__file__))
input_file = f"{directory}/day1_input.txt"

def part1():
    number_list = []
    with open(input_file, 'r') as f:
        for line in f.read().splitlines():
            numbers = ''.join(c for c in line if c.isdigit())
            number_list.append(int(f"{numbers[:1]}{numbers[-1:]}"))
    return(sum(number_list))

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

def part2():
    with open(input_file, 'r') as f:
        numbers = []
        for line in f.read().splitlines():
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
        return(sum(numbers))
            
def main():
    part1_result = part1()
    print(f"Part 1 answer: {part1_result}")
    part2_result = part2()
    print(f"Part 2 answer: {part2_result}")

if __name__ == "__main__":
    main()