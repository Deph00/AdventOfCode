import re

sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        matches = re.findall(r"mul\((\d+),(\d+)\)",line)
        for match in matches:
            x, y = match
            print(f"x: {x}, y: {y}")
            sum += int(x)*int(y)


print(sum)