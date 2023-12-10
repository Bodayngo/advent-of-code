import os
from itertools import cycle
from math import lcm

def parse_input(input_lines):
    directions = input_lines.pop(0).replace('L', '0').replace('R', '1')
    locations = {var.strip(): tuple(val.strip() for val in expr[1:-1].split(', ')) 
                for line in input_lines[1:]
                for var, expr in (line.split(' = '),)}
    return directions, locations

def get_steps(start_location, locations, directions, part2=False):
    current_location = start_location
    for index, direction in enumerate(cycle(directions), start=1):
        current_location = locations[current_location][int(direction)]
        if (current_location[-1] == 'Z' and part2) or (current_location == 'ZZZ' and not part2):
            return index

def part1(directions, locations):
    total_steps = get_steps('AAA', locations, directions)
    return total_steps

def part2(directions, locations):
    start_locations = {key: {'steps': 0} for key in locations.keys() if key[-1] == 'A'}
    for start_location in start_locations.keys():
        total_steps = get_steps(start_location, locations, directions, part2=True)
        start_locations[start_location]['steps'] = total_steps
    total_steps_list = [start_locations[key]['steps'] for key in start_locations.keys()]
    return lcm(*total_steps_list)

def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{directory}/puzzle_input.txt"
    with open(input_file, 'r') as file:
        input_lines = file.read().strip().splitlines()
    directions, locations = parse_input(input_lines)
    print(f"Part 1 answer: {part1(directions, locations)}")
    print(f"Part 2 answer: {part2(directions, locations)}")
 
if __name__ == '__main__':
    main()
