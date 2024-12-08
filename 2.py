import sys
import os
import numpy as np

print(__file__)
input_file = sys.argv[1] if len(sys.argv)>1 else __file__.replace(".py",".ex")
if not os.path.exists(input_file):
    sys.exit(f"{input_file} not found")

data = open(input_file).read().strip().split('\n')
R,C = len(data),len(data[0])
##################################################

def is_safe(nums):
    d = np.diff(nums)
    if (d<0).sum()==0 or (d>0).sum()==0:
        if min(abs(d))>=1 and max(abs(d))<=3:
            return True
    return False

ans1=ans2=0
for line in  data:
    nums = [int(x) for x in line.split()]
    if is_safe(nums):
        ans1 += 1
        
    for i in range(len(nums)):
        if is_safe(nums[:i] + nums[i+1:]):
            ans2 += 1
            break    

print("Part 1: ",ans1)
print("Part 2: ",ans2)




