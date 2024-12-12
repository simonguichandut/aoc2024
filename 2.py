from utils import *
import numpy as np

data = read_lines()

def is_safe(n):
    d = np.diff(n)
    if (d<0).sum()==0 or (d>0).sum()==0:
        if min(abs(d))>=1 and max(abs(d))<=3:
            return True
    return False

ans1=ans2=0
for line in  data:
    n = nums(line)
    if is_safe(n):
        ans1 += 1
        
    for i in range(len(n)):
        if is_safe(n[:i] + n[i+1:]):
            ans2 += 1
            break    

print("Part 1: ",ans1)
print("Part 2: ",ans2)