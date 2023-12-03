import os
import re

directory = os.path.dirname(os.path.realpath(__file__))
input_file = f"{directory}/day3_input.txt"

def part1():
    valid_number_sum = 0
    with open(input_file, 'r') as f:
        all_number_matches = []
        input_lines = f.read().splitlines()
        # Get numbers
        for line in input_lines:
            line_number_matches = []
            nunmber_matches = re.finditer(r"[0-9]+", line)
            for match in nunmber_matches:
                number_match = (match.group(), match.start(), match.end())
                line_number_matches.append(number_match)
            all_number_matches.append(line_number_matches)
        # Check if numbers are adjacent to symbols
        for line, number_matches in enumerate(all_number_matches):
            for number_match in number_matches:
                valid = False
                #print(str(line) + ': ' + str(number_match))
                for l in range(-1, 2):
                    if line+l >= 0 and line+l < len(input_lines):
                        #print(input_lines[line+l])
                        symbol_results = re.finditer(r"[^\d.]", input_lines[line+l])
                        for symbol in symbol_results:
                            #print(symbol)
                            if symbol.start() >= number_match[1]-1 and symbol.start() <= number_match[2]:
                                valid = True
                if valid == True:
                    valid_number_sum+=int(number_match[0])
        return(valid_number_sum)


def main():
    part1_result = part1()
    print(f"Part 1 answer: {part1_result}")

if __name__ == '__main__':
    main()