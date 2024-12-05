safe = 0

with open('input.txt', 'r') as file:
    for line in file:
        values = line.split()
        increase = True
        decrease = True
        spacing = True
        for a, b in zip(values, values[1:]): # many ifs but it works
            if int(a) < int(b):
                decrease = False
            if int(a) > int(b):
                increase = False
            if abs(int(a) - int(b)) == 0 or abs(int(a) - int(b)) > 3:
                spacing = False
        if (decrease or increase) and spacing:
            safe += 1
            print(line)


print(safe)