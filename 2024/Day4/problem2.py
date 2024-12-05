def checkDirection(matrix, seq, row, col, rowIncrease, colIncrease):
    try:
        for i, char in enumerate(seq):
            newRow = row + (rowIncrease*(i+1))
            newCol = col + (colIncrease*(i+1))
            if newRow == -1 or newCol == -1:
                return False
            elif matrix[newRow][newCol] != char:
                return False
        return True
    except IndexError:
        return False

def checkMOrS(matrix, row, col, rowIncrease, colIncrease):
    try:
        rowValue = matrix[row + rowIncrease][col]
        colValue = matrix[row][col + colIncrease]
        if colValue == rowValue:
            return 0
        if colValue != "S" and colValue != "M":
            return 0
        if rowValue != "S" and rowValue != "M":
            return 0
        if colIncrease == -2 and colValue == "M":
            return 0
        print("row " + str(row) + " col " + str(col))
        return 1
    except IndexError:
        return 0


sum = 0
row = 0

with open('input.txt', 'r') as file:
    matrix = [list(line.strip()) for line in file]
    for row_index, row in enumerate(matrix):        # Outer loop for rows
        for col_index, element in enumerate(row):   # Inner loop for elements in the row
            if element == 'M':
                if checkDirection(matrix, 'AS', row_index, col_index, 1, 1):
                    sum += checkMOrS(matrix, row_index, col_index, 2, 2)
                if checkDirection(matrix, 'AS', row_index, col_index, 1, -1):
                    sum += checkMOrS(matrix, row_index, col_index, 2, -2)
                if checkDirection(matrix, 'AS', row_index, col_index, -1, 1) and matrix[row_index][col_index+2] == "M" and matrix[row_index-2][col_index] == "S":
                    sum += 1



print(sum)