from utils import *

data = read_lines()

l1 = sorted([nums(line)[0] for line in data])
l2 = sorted([nums(line)[1] for line in data])

print("Part 1: ", sum(abs(a-b) for a,b in zip(l1,l2)))
print("Part 1: ", sum(a*l2.count(a) for a in l1))