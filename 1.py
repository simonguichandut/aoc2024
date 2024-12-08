import sys
import os

print(__file__)
input_file = sys.argv[1] if len(sys.argv)>1 else __file__.replace(".py",".ex")
if not os.path.exists(input_file):
    sys.exit(f"{input_file} not found")

data = open(input_file).read().strip().split('\n')
R,C = len(data),len(data[0])
##################################################

l1 = [int(line.split()[0]) for line in data]
l2 = [int(line.split()[1]) for line in data]
ans = 0
for i in range(len(l1)):
    a,b = min(l1),min(l2)
    l1.remove(a)
    l2.remove(b)
    ans += abs(a-b)

print("Part 1: ",ans)

l1 = [int(line.split()[0]) for line in data]
l2 = [int(line.split()[1]) for line in data]
ans = 0
for a in l1:
    ans += a*l2.count(a)

print("Part 2: ", ans)



