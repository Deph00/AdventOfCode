
file_indices = []
space_indices = []

blocks = []

def move_and_calculate():
    sum = 0
    for i, val in enumerate(blocks):
        if val != '.':
            sum += int(val) * i
        else:
            if i <= file_indices[-1]:
                sum += int(blocks[file_indices[-1]]) * i
                blocks[file_indices[-1]] = '.'
                del file_indices[-1]
    return sum


with open('input.txt', 'r') as file:
    file_id = 0
    block_index = 0
    for i, val in enumerate(file.readline().strip()):
        disk_value = int(val.strip())
        if i % 2 == 0: #file
            blocks += [str(file_id)] * disk_value
            for i in range(disk_value):
                file_indices.append(block_index + i)
            block_index += disk_value
            file_id += 1
        else:
            blocks.extend(['.'] * disk_value)
            for i in range(disk_value):
                space_indices.append(block_index + i)
            block_index += disk_value

    sum = move_and_calculate()

print(sum)