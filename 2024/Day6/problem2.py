matrix = []
dots_to_check = set()
sum = 0

movements = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)}

next_direction = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'}

def read_file_and_find_guard(file):
    direction, g_row, g_col = '', -1, -1
    for i, line in enumerate(file):
        row = list(line.strip())
        matrix.append(row)
        for j, val in enumerate(row):
            if val in movements.keys(): # checks if the guard is there, and return it
                direction, g_row, g_col = val, i, j
    return direction, g_row, g_col

def mark_path(row, col, get_dots):
    value = matrix[row][col]
    if value != 'X':
        if get_dots:
            dots_to_check.add((row, col))
        matrix[row][col] = 'X'
        return 1
    else:
        return 0

def move_guard(dir, row, col):
    direction = movements[dir]
    new_row = row + direction[0]
    new_col = col + direction[1]
    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):  # Ensure within bounds
        in_front = matrix[new_row][new_col]
        if in_front == "#":
            return next_direction[dir], row, col # if obstacle, we turn
        else:
            return dir, new_row, new_col # if no obstacle, we move
    else:
        return dir, -1, -1 # we outside

def simulate_guard(dir, row, col, get_dots):
    positions = []
    while row != -1 and col != -1:
        if (dir, row, col) in positions:
            return 1
        positions.append((dir, row, col))
        mark_path(row, col, get_dots)
        dir, row, col = move_guard(dir, row, col)
    return 0

with open('input.txt', 'r') as file:
    dir, row, col = read_file_and_find_guard(file) # reads file and gets starting position
    simulate_guard(dir, row, col, True)
    dots_to_check.remove((row, col)) # remove starting position
    for i, dot in enumerate(dots_to_check):
        matrix[dot[0]][dot[1]] = '#' # who cares about new symbols, add obstacle
        sum += simulate_guard(dir, row, col, False)
        matrix[dot[0]][dot[1]] = '.' # reset obstacle

print(sum)