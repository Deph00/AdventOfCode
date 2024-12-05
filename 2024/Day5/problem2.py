from collections import defaultdict

rule_behind = defaultdict(list)

sum = 0

def is_behind(behind_list, i, updates):
    for update in updates[i+1:]:
        if update in behind_list:
            return False
    return True

def is_correct(updates):
    correct = True
    for i, update in enumerate(updates): # goes through every element in row
        if not is_behind(rule_behind[update], i, updates): #
            correct = False
            break
    if correct and len(updates) > 1:
        return True

def reorder_list(updates):
    list = []
    failed_list = updates
    while len(failed_list) > 0:
        if len(failed_list) == 1:
            list += failed_list
            del failed_list[0]
        else:
            element = failed_list[0]
            if is_behind(rule_behind[element], 0, failed_list):
                list.append(element)
                del failed_list[0]
            else:
                removed_element = failed_list.pop(0)
                failed_list.append(removed_element)

    return list


with open('input.txt', 'r') as file:
    for line in file:
        rules = line.strip().split('|')
        if len(rules) == 2:
            rule_behind[rules[1]].append(rules[0])
        else:
            updates = line.strip().split(',')
            if not is_correct(updates) and len(updates) > 1: # if row is not correct
                reordered = reorder_list(updates) # reorder the list
                middle_index = len(reordered) // 2
                sum += int(reordered[middle_index])
print(sum)