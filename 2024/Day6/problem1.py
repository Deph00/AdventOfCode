matrix = []
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
    guard = []
    for i, line in enumerate(file):
        row = list(line.strip())
        matrix.append(row)
        for j, val in enumerate(row):
            if val in movements.keys(): # checks if the guard is there, and return it
                guard = [val, i, j]
    return guard

def mark_path(guard):
    value = matrix[guard[1]][guard[2]]
    if value != 'X':
        matrix[guard[1]][guard[2]] = 'X'
        return 1
    else:
        return 0

def move_guard(guard):
    direction = movements[guard[0]]
    in_front = matrix[guard[1] + direction[0]][guard[2] + direction[1]]
    if in_front == "#":
        guard[0] = next_direction[guard[0]]
    else:
        guard[1] = guard[1] + direction[0]
        guard[2] = guard[2] + direction[1]

with open('input.txt', 'r') as file:
    guard = read_file_and_find_guard(file) # ('^', 6, 4)
    while guard[1] != -1 and guard[2] != -1:
        try:
            sum += mark_path(guard)
            move_guard(guard)
        except IndexError:
            guard[1] = -1

print(sum)