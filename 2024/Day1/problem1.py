list1 = []
list2 = []

with open('input.txt', 'r') as file:
    for line in file:
        values = line.split()
        list1.append(values[0])
        list2.append(values[1])


list1.sort()
list2.sort()

sum = 0

for val, val2 in zip(list1, list2):
    sum += abs(int(val) - int(val2))

print(sum)