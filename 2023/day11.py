import os

directory = os.path.dirname(os.path.realpath(__file__))
input_file = f"{directory}/puzzle_input.txt"

def part1():
    pass

def part2():
    pass

def main():
    with open(input_file, 'r') as file:
        input = file.read().strip()
        #input_lines = file.read().strip().splitlines()
    print(f"Part 1 answer: {part1(input)}")
    print(f"Part 2 answer: {part2(input)}")
 
if __name__ == '__main__':
    main()
