def is_safe(values):
    increase = True
    decrease = True
    spacing = True
    for a, b in zip(values, values[1:]):
        if int(a) < int(b):
            decrease = False
        if int(a) > int(b):
            increase = False
        if abs(int(a) - int(b)) == 0 or abs(int(a) - int(b)) > 3:
            spacing = False
    if (decrease or increase) and spacing:
        return True
    else:
        return False

safe = 0
k = 4

with open('input.txt', 'r') as file:
    for line in file:
        values = line.split()
        sublists = [values[:i] + values[i+1:] for i in range(len(values))]
        for sublist in sublists:
            if is_safe(sublist):
                safe += 1
                print(values)
                break

print(safe)