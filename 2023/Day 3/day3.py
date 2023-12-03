import os
import re

directory = os.path.dirname(os.path.realpath(__file__))
input_file = f"{directory}/day3_input.txt"

def part1():
    valid_number_sum = 0
    with open(input_file, 'r') as f:
        all_number_matches = []
        input_lines = f.read().splitlines()
        for line in input_lines:
            line_number_matches = []
            nunmber_matches = re.finditer(r"[0-9]+", line)
            for match in nunmber_matches:
                number_match = (match.group(), match.start(), match.end())
                line_number_matches.append(number_match)
            all_number_matches.append(line_number_matches)
        for line, number_matches in enumerate(all_number_matches):
            for number_match in number_matches:
                valid = False
                for l in range(-1, 2):
                    if line+l >= 0 and line+l < len(input_lines):
                        symbol_results = re.finditer(r"[^\d.]", input_lines[line+l])
                        for symbol in symbol_results:
                            if symbol.start() >= number_match[1]-1 and symbol.start() <= number_match[2]:
                                valid = True
                if valid == True:
                    valid_number_sum += int(number_match[0])
        return(valid_number_sum)
    
def part2():
    valid_number_sum = 0
    with open(input_file, 'r') as f:
        all_symbol_matches = []
        input_lines = f.read().splitlines()
        for line in input_lines:
            line_symbol_matches = []
            symbol_matches = re.finditer(r"[*]", line)
            for match in symbol_matches:
                line_symbol_matches.append(match.start())
            all_symbol_matches.append(line_symbol_matches)
        for line, symbol_matches in enumerate(all_symbol_matches):
            for symbol_match in symbol_matches:
                adj_numbers = []
                for l in range(-1, 2):
                    if line+l >= 0 and line+l < len(input_lines):
                        number_matches = re.finditer(r"[0-9]+", input_lines[line+l])
                        for number_match in number_matches:
                            if symbol_match >= number_match.start()-1 and symbol_match <= number_match.end():
                                adj_numbers.append(number_match.group())
                if len(adj_numbers) == 2:
                    ratio = int(adj_numbers[0]) * int(adj_numbers[1])
                    valid_number_sum += ratio
        return valid_number_sum

def main():
    part1_result = part1()
    print(f"Part 1 answer: {part1_result}")
    part2_result = part2()
    print(f"Part 2 answer: {part2_result}")

if __name__ == '__main__':
    main()