from collections import defaultdict

rule_behind = defaultdict(list)

sum = 0

def is_behind(behind_list, i, updates):
    for update in updates[i+1:]:  # checks if rest of list is in the list it CANT be behind
        if update in behind_list:
            return False
    return True

def is_correct(updates):
    correct = True
    for i, update in enumerate(updates): # goes through every element in row
        if not is_behind(rule_behind[update], i, updates): # if rest of list overlaps with list of DONTS
            correct = False
            break
    if correct and len(updates) > 1: # length is lazy way to skip newlines and empty strings
        return True

with open('input.txt', 'r') as file:
    for line in file:
        rules = line.strip().split('|')
        if len(rules) == 2:
            rule_behind[rules[1]].append(rules[0]) # creates map of every value, the key CANT be behind
        else:
            updates = line.strip().split(',')
            if is_correct(updates) and len(updates) > 1: # if row is not correct
                middle_index = len(updates) // 2
                sum += int(updates[middle_index])

print(sum)