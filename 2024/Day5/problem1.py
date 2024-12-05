from collections import defaultdict

rule_ahead = defaultdict(list)
rule_behind = defaultdict(list)

sum = 0

def isBehind(behind_list, i, updates):
    for update in updates[i+1:]:
        if update in behind_list:
            return False
    return True

with open('input.txt', 'r') as file:
    for line in file:
        rules = line.strip().split('|')
        if len(rules) == 2:
            rule_ahead[rules[0]].append(rules[1])
            rule_behind[rules[1]].append(rules[0])
        else:
            updates = line.strip().split(',')
            correct = True
            for i, update in enumerate(updates):
                if not isBehind(rule_behind[update], i, updates):
                    correct = False
                    break
            if correct and len(updates) > 1:
                middle_index = len(updates) // 2
                sum += int(updates[middle_index])

print(sum)