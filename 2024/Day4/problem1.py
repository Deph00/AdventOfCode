def checkDirection(matrix, seq, row, col, rowIncrease, colIncrease):
    try:
        for i, char in enumerate(seq):
            newRow = row + (rowIncrease*(i+1))
            newCol = col + (colIncrease*(i+1))
            if newRow == -1 or newCol == -1:
                return 0
            elif matrix[newRow][newCol] != char:
                return 0
        return 1
    except IndexError:
        return 0


sum = 0
row = 0

with open('input.txt', 'r') as file:
    matrix = [list(line.strip()) for line in file]
    for row_index, row in enumerate(matrix):        # Outer loop for rows
        for col_index, element in enumerate(row):   # Inner loop for elements in the row
            if element == 'X':
                sum += checkDirection(matrix, 'MAS', row_index, col_index, 0, -1)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, 0, 1)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, -1, 0)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, 1, 0)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, 1, 1)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, 1, -1)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, -1, 1)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, -1, -1)


print(sum)