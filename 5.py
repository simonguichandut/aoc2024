import sys
import os

print(__file__)
input_file = sys.argv[1] if len(sys.argv)>1 else __file__.replace(".py",".ex")
if not os.path.exists(input_file):
    sys.exit(f"{input_file} not found")

data = open(input_file).read().strip().split('\n')
##################################################

reading_rules = True
rules,updates = [],[]
for line in  data:
    if '|' not in line:
        reading_rules = False
    if reading_rules:
        rules.append(list(map(int, line.split('|'))))
    else:
        if len(line)>=1:
            updates.append(list(map(int, line.split(','))))

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



