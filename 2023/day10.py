import os

directory = os.path.dirname(os.path.realpath(__file__))
input_file = f"{directory}/puzzle_input.txt"

def process_input(input):
    return [list(row) for row in input.split('\n') if row]


class Grid:
    def __init__(self, input_lines):
        self.grid = input_lines
        self.max_col_index = len(max(self.grid, key=len)) - 1
        self.max_row_index = len(self.grid) - 1
        self.pipe_connections = {'|': ('N', 'S'), '-': ('E', 'W'), 'L': ('N', 'E'), 'J': ('N', 'W'), '7': ('S', 'W'), 'F': ('S', 'E')}
        self.start_position = self.get_starting_position()

    def get_starting_position(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == 'S':
                    return y, x
                
    def get_neighbor_positions(self, position):
        y, x = position
        adjacent_positions = []
        if y > 0:
            adjacent_positions.append((y - 1, x))
        if y < self.max_col_index:
            adjacent_positions.append((y + 1, x))
        if x > 0:
            adjacent_positions.append((y, x - 1))
        if x < self.max_row_index:
            adjacent_positions.append((y, x + 1))
        return adjacent_positions
    
    def get_valid_neighbors(self, position):
        pipe =  self.grid[position[0]][position[1]]
        valid_neighbors = []
        for neighbor_position in self.get_neighbor_positions(position):
            neighbor_pipe = self.grid[neighbor_position[0]][neighbor_position[1]]
            if neighbor_pipe in self.pipe_connections.keys() and self.check_connection(pipe, position, neighbor_pipe, neighbor_position):
                valid_neighbors.append(neighbor_position)
        return valid_neighbors
    
    def check_connection(self, pipe1, pipe1_pos, pipe2, pipe2_pos):
        delta_y = pipe1_pos[0] - pipe2_pos[0]
        delta_x = pipe1_pos[1] - pipe2_pos[1]
        positions = {(0, 1): 'left', (0, -1): 'right', (1, 0): 'up',(-1, 0): 'down'}
        pipe2_position = positions.get((delta_y, delta_x))
        if pipe2_position == 'left':
            if pipe1 == 'S' and 'E' in self.pipe_connections[pipe2]:
                return True
            elif pipe1 == 'S':
                return False
            elif 'W' in self.pipe_connections[pipe1] and 'E' in self.pipe_connections[pipe2]:
                return True
        elif pipe2_position == 'right':
            if pipe1 == 'S' and 'W' in self.pipe_connections[pipe2]:
                return True
            elif pipe1 == 'S':
                return False
            elif 'E' in self.pipe_connections[pipe1] and 'W' in self.pipe_connections[pipe2]:
                return True
        elif pipe2_position == 'up':
            if pipe1 == 'S' and 'S' in self.pipe_connections[pipe2]:
                return True
            elif pipe1 == 'S':
                return False
            elif 'N' in self.pipe_connections[pipe1] and 'S' in self.pipe_connections[pipe2]:
                return True
        elif pipe2_position == 'down':
            if pipe1 == 'S' and 'N' in self.pipe_connections[pipe2]:
                return True
            elif pipe1 == 'S':
                return False
            elif 'S' in self.pipe_connections[pipe1] and 'N' in self.pipe_connections[pipe2]:
                return True
        return False


def has_duplicates(input_list: list[tuple]) -> bool:
    seen = set()
    for item in input_list:
        if item in seen:
            return True
        seen.add(item)
    return False

def part1(input):
    input_lines = process_input(input)
    grid = Grid(input_lines)
    tracker = [[grid.start_position]]
    steps_counter = 0
    while True:
        next_neighbors = []
        for position in tracker[steps_counter]:
            next_neighbors.extend(grid.get_valid_neighbors(position))
        filtered_next_neighbors = [item for item in next_neighbors if item not in tracker[steps_counter - 1]]
        tracker.append(filtered_next_neighbors)
        steps_counter += 1
        if has_duplicates(filtered_next_neighbors):
            break
    return steps_counter

def main():
    with open(input_file, 'r') as file:
        input = file.read().strip()
    print(f"Part 1 answer: {part1(input)}")
 
if __name__ == '__main__':
    main()
