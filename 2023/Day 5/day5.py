import os

###############################################################################
##  Part 1
###############################################################################
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


def get_mapped_values(input_values: int, mappings: list[tuple]):
    mapped_values = []
    for input_value in input_values:
        mapping_override = False
        override_maps = []
        for mapping in mappings:
            if mapping[1] <= input_value <= mapping[1] + mapping[2]:
                mapping_override = True
                override_maps.append(mapping)
        if mapping_override:
            for map in override_maps:
                offset = map[0] - map[1]
                mapped_value = input_value + offset
                mapped_values.append(mapped_value)
        else:
            mapped_values.append(input_value)
    return mapped_values

#60 56 37
def part1():
    """
    (dest_range_start, src_range_start, range_len)
    """
    seeds, mappings_dict = parse_input()
    seed = [14]
    for mapping_name, mappings in mappings_dict.items():
        print(f"Mapping name: {mapping_name}")
        print(mappings)
        seed = get_mapped_values(seed, mappings)
        print(seed)
#    for seed in seeds:
#        print(f"Seed: {seed}")
#        print(get_mapped_value(seed, mappings_dict['seed-to-soil']))
#        for mapping_name, mappings in mappings_dict.items():
#            print(f"Mapping name: {mapping_name}")
#            seed = get_mapped_value(seed, mappings)
#            print(seed)



def main():
    part1()
    #part1_result = part1()
    #print(f"Part 1 answer: {part1_result}")
    #part2_result = part2()
    #print(f"Part 2 answer: {part2_result}")

if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{directory}/test_input.txt"
    with open(input_file, 'r') as file:
        input = file.read().strip()

    main()