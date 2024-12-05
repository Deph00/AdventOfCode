list1 = []
list2 = []

with open('input.txt', 'r') as file:
    for line in file:
        values = line.split()
        list1.append(values[0])
        list2.append(values[1])

similarty_score = 0

for val in list1:
    similarty_score += int(val) * list2.count(val)

print(similarty_score)