import os


def parse_input():
    mappings_dict = {}
    sections = input.split('\n\n')
    seeds = [eval(i) for i in sections.pop(0).split(':')[1].strip().split(' ')]
    for section in sections:
        lines = [
            line
            for line in section.splitlines()
        ]
        mapping_name = lines.pop(0).split(' ')[0]
        mappings = [
            tuple(map(int, mapping.split()))
            for mapping in lines
        ]
        mappings_dict[mapping_name] = mappings

    return seeds, mappings_dict


def get_mapped_value(input_value: int, mappings: list[tuple]):
    mapping_override = False
    for mapping in mappings:
        if mapping[1] <= input_value <= mapping[1] + mapping[2] - 1:
            mapping_override = True
            map = mapping
    if mapping_override:
        offset = map[0] - map[1]
        output_value = input_value + offset
    else:
        output_value = input_value

    return input_value


def part1():
    seeds, mappings_dict = parse_input()
    locations = []
    for seed in seeds:
        for mapping_name, mappings in mappings_dict.items():
            seed = get_mapped_value(seed, mappings)
        locations.append(seed)

    return min(locations)


def main():
    part1_result = part1()
    print(f"Part 1 answer: {part1_result}")
    #part2_result = part2()
    #print(f"Part 2 answer: {part2_result}")

if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{directory}/day5_input.txt"
    with open(input_file, 'r') as file:
        input = file.read().strip()

    main()
