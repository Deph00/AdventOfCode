# checks if MAS is in a certain direction
def checkDirection(matrix, seq, row, col, rowIncrease, colIncrease):
    try:
        for i, char in enumerate(seq): # Iterate through MAS
            newRow = row + (rowIncrease*(i+1)) # moves in a certain direction
            newCol = col + (colIncrease*(i+1))
            if newRow == -1 or newCol == -1: # If outside of matrix, exit
                return 0
            elif matrix[newRow][newCol] != char: # IF NOT THE CORRECT LETTER
                return 0
        return 1
    except IndexError:
        return 0


sum = 0

with open('input.txt', 'r') as file:
    matrix = [list(line.strip()) for line in file]
    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if element == 'X': # CTRL D IS FASTER THAN WRITING A LOOP, DONT GET MAD
                sum += checkDirection(matrix, 'MAS', row_index, col_index, 0, -1)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, 0, 1)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, -1, 0)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, 1, 0)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, 1, 1)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, 1, -1)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, -1, 1)
                sum += checkDirection(matrix, 'MAS', row_index, col_index, -1, -1)


print(sum)