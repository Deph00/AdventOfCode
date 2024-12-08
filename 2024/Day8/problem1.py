from collections import defaultdict
import itertools

sum = 0
antennas = defaultdict(list)

matrix = []
freqs = set()

def within_bounds(freq):
    return 0 <= freq[0] < len(matrix[0]) and 0 <= freq[1] < len(matrix)

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

            freq1 = ((pair[0][0] + x_diff), (pair[0][1] + y_diff))
            freq2 = ((pair[1][0] - x_diff), (pair[1][1] - y_diff))
            if within_bounds(freq1):
                freqs.add(freq1)

            if within_bounds(freq2):
                freqs.add(freq2)

print(len(freqs))
