from itertools import product
import re

def calculate(values, operators):
    result = values[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += values[i + 1]
        elif operator == '*':
            result *= values[i + 1]
    return result

def is_valid_equation(target, values):
    n = len(values)
    for operators in product(['+', '*'], repeat=n-1): # generates combinations of operations
        if calculate(values, operators) == target: # if target equals this combination
            return True
    return False

sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        equation = re.split(r'[: ]', line.strip())
        target, values = int(equation[0]), [int(val) for val in equation[2:]] # takes the expected answer, and the rest of the numbers
        if is_valid_equation(target, values): # if the same, we add it
            sum += target

print(sum)
