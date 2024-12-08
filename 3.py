import sys
import os
import re
print(__file__)

input_file = sys.argv[1] if len(sys.argv)>1 else __file__.replace(".py",".ex")
if not os.path.exists(input_file):
    sys.exit(f"{input_file} not found")

txt = open(input_file).read().strip()
##################################################

ans = 0
for mul in re.findall("mul\(\d+,\d+\)", txt):
    nums = list(map(int,mul.split("mul(")[1][:-1].split(',')))
    ans += nums[0]*nums[1]

print("Part 1: ", ans)

# Part 2 : really gross!!!
do = True
a,b = 0,0
ans2 = 0
while b < len(txt):
    if do:
        if "don't()" not in txt[a:]:
            b = len(txt)
        else:
            b = a + txt[a:].index("don't()")

        for mul in re.findall("mul\(\d+,\d+\)", txt[a:b]):
            nums = list(map(int,mul.split("mul(")[1][:-1].split(',')))
            ans2 += nums[0]*nums[1]
        do = False
        a = b+7

    else:
        if "do()" not in txt[a:]:
            break
        b = a + txt[a:].index("do()")
        do = True
        a = b+4

print("Part 2: ",ans2)



