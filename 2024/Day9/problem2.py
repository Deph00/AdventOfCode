def calculate(blocks):
    sum = 0
    for i, val in enumerate(blocks):
        if val != '.':
            sum += int(val) * i
    return sum

def move_and_calculate(blocks, file_blocks, space_blocks):
    for file in file_blocks:
        file_start, file_end = file
        width_of_file = file_end - file_start + 1

        for i, space in enumerate(space_blocks):
            space_start, space_end = space
            width_of_space = space_end - space_start + 1
            if width_of_space > width_of_file:
                blocks[space_start:space_end+width_of_file] = blocks[file_start:file_end + 1]
                blocks[file_start:file_end + 1] = ['.'] * width_of_file

                if width_of_space > width_of_file:
                    space_blocks[i] = (space_start + width_of_file, space_end)
                else:
                    space_blocks.pop(i)
                break
    return calculate(blocks)

def parse(input_line):
    blocks = []
    file_blocks = []
    space_blocks = []
    file_id = 0
    block_index = 0
    for i, val in enumerate(input_line):
        disk_value = int(val)
        if i % 2 == 0: #file
            blocks.extend([str(file_id)] * disk_value)
            file_blocks.insert(0, (block_index, block_index + disk_value - 1))
            file_id += 1
        else:
            blocks.extend(['.'] * disk_value)
            space_blocks.append((block_index, block_index + disk_value - 1))
        block_index += disk_value
    return blocks, file_blocks, space_blocks

with open('input.txt', 'r') as file:
    input_line = file.readline().strip()

blocks, file_blocks, space_blocks = parse(input_line)
sum = move_and_calculate(blocks, file_blocks, space_blocks)

print(sum)