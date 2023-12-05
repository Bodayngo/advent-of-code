import os

# File input
directory = os.path.dirname(os.path.realpath(__file__))
input_file = f"{directory}/test_input.txt"
with open(input_file, 'r') as file:
    input = file.read().strip()

###############################################################################
##  Part 1
###############################################################################
def get():
    mappings = {}
    sections = input.split('\n\n')
    for section in sections:
        

def part1():
    get()

def main():
    part1()
    #part1_result = part1()
    #print(f"Part 1 answer: {part1_result}")
    #part2_result = part2()
    #print(f"Part 2 answer: {part2_result}")

if __name__ == '__main__':
    main()