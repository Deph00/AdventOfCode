from collections import defaultdict
import itertools

sum = 0
antennas = defaultdict(list)

matrix = []
freqs = set()

def within_bounds(freq):
    return 0 <= freq[0] < len(matrix[0]) and 0 <= freq[1] < len(matrix)

def add_freqs(pair, x_diff, y_diff):
    i = 0
    while True:
        freq1 = ((pair[0][0] + (x_diff*i)), (pair[0][1] + (y_diff*i)))
        if within_bounds(freq1):
            freqs.add(freq1)
            i += 1
        else:
            break
    i = 0
    while True:
        freq2 = ((pair[1][0] - (x_diff*i)), (pair[1][1] - (y_diff*i)))
        if within_bounds(freq2):
            freqs.add(freq2)
            i += 1
        else:
            break

with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        row = list(line.strip())
        matrix.append(row)
        for j, char in enumerate(line.strip()):
            if char != '.':
                antennas[char].append((i, j))

    for key in antennas.keys():
        values = antennas[key]
        pairs = list(itertools.combinations(values, 2))
        for i, pair in enumerate(pairs):
            x_diff = pair[0][0] - pair[1][0]
            y_diff = pair[0][1] - pair[1][1]

            add_freqs(pair, x_diff, y_diff)

print(len(freqs))
