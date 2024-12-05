import re

sum = 0
enabled = True

with open('input.txt', 'r') as file:
    for line in file:
        matches = re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)",line)
        for match in matches:
            x, y, do, dont = match
            if do:
                enabled = True
            elif dont:
                enabled = False
            elif enabled:
                print(f"x: {x}, y: {y}")
                sum += int(x)*int(y)

print(sum)