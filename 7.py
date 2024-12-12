from utils import *
from itertools import product

data = read_lines()
R,C = len(data),len(data[0])

# Pre-create all the possible lists of operations, up to 12 max operations based on looking at the input
all_ops = {n:list(product('+*', repeat=n)) for n in range(12)}
all_ops_concat = {n:[ops for ops in list(product('+*|', repeat=n)) if '|' in ops] for n in range(12)}

def is_valid(tot, nums, concat=False):
    ops = all_ops_concat[len(nums)-1] if concat else all_ops[len(nums)-1]
    for op in ops:
        res = nums[0]
        for i,num in enumerate(nums[1:]):
            if op[i] == '+':
                res += num
            elif op[i] == '*':
                res *= num
            elif concat and op[i] == '|':
                res  = int(str(res)+str(num))
        if res == tot:
            return True
    return False

ans1 = ans2 = 0
for line in  data:
    tot,nums = line.split(': ')
    tot = int(tot)
    nums = list(map(int, nums.split()))
    if is_valid(tot, nums):
        ans1 += tot
        ans2 += tot
    else:
        if is_valid(tot, nums, concat=True):
            ans2 += tot

print("Part 1: ", ans1)
print("Part 2: ", ans2)