import os

def parse_input(input_data):
    mappings_dict = {}
    sections = input_data.split('\n\n')
    seeds = [int(i) for i in sections.pop(0).split(':')[1].strip().split(' ')]
    for section in sections:
        lines = section.splitlines()
        mapping_name = lines[0].split(' ')[0]
        mappings = [tuple(map(int, mapping.split())) for mapping in lines[1:]]
        mappings_dict[mapping_name] = mappings
    return seeds, mappings_dict

def get_mapped_value(input_value, mapping):
    for map_item in mapping:
        if map_item[1] <= input_value <= map_item[1] + map_item[2] - 1:
            offset = map_item[0] - map_item[1]
            return input_value + offset
    return input_value

def part1(input_data):
    seeds, mappings_dict = parse_input(input_data)
    locations = []
    for seed in seeds:
        for _, mappings in mappings_dict.items():
            seed = get_mapped_value(seed, mappings)
        locations.append(seed)
    return min(locations)

"""
def part2():
    seeds_list, mappings_dict = parse_input()
    locations = []
    for seed_start, seed_range in zip(seeds_list[::2], seeds_list[1::2]):
        for seed in range(seed_start, seed_start + seed_range):
            for _, mappings in mappings_dict.items():
                seed = get_mapped_value(seed, mappings)
            locations.append(seed)
    return min(locations)
"""

def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{directory}/day5_input.txt"
    with open(input_file, 'r') as file:
        input_data = file.read().strip()
    print(f"Part 1 answer: {part1(input_data)}")

if __name__ == '__main__':
    main()
