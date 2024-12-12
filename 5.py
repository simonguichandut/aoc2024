from utils import *

rules, updates = read().split('\n\n')

rules = [nums(rule) for rule in rules.split('\n')]
updates = [nums(update) for update in updates.split('\n')]

ans1 = ans2 = 0
for update in updates:
    valid = True
    for i in range(len(update)-1):
        for j in range(i,len(update)):
            if [update[j],update[i]] in rules:
                valid = False

    if valid:
        ans1 += update[len(update)//2]
    else:
        while True:
            did_swap = False
            for i in range(len(update)-1):
                for j in range(i,len(update)):
                    if [update[j],update[i]] in rules:
                        update[i],update[j] = update[j],update[i]
                        did_swap = True
            if not did_swap:
                break
        ans2 += update[len(update)//2]

print("Part 1: ", ans1)
print("Part 2: ", ans2)