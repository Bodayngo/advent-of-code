import os
import math

def parse_input(puzzle_input):
    lines = puzzle_input.splitlines()
    race_times = [eval(i) for i in str.split(lines[0])[1:]]
    record_distances = [eval(i) for i in str.split(lines[1])[1:]]
    return race_times, record_distances

def calculate_winning_combinations(race_time, record_distance):
    winning_combinations = sum(1 for ms in range(0, race_time + 1) if ms * (race_time - ms) > record_distance)
    return winning_combinations

def part1(input):
    race_times, record_distances = parse_input(input)
    winning_combinations_per_race = [
        calculate_winning_combinations(rt, rd) for rt, rd in zip(race_times, record_distances)
    ]
    return math.prod(winning_combinations_per_race)

def part2(input):
    race_times, record_distances = parse_input(input)
    race_time = int(''.join(map(str, race_times)))
    record_distance = int(''.join(map(str, record_distances)))
    winning_combinations = calculate_winning_combinations(race_time, record_distance)
    return winning_combinations

def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{directory}/day6_input.txt"
    with open(input_file, 'r') as file:
        input = file.read().strip()
    print(f"Part 1 answer: {part1(input)}")
    print(f"Part 2 answer: {part2(input)}")
 
if __name__ == '__main__':
    main()
