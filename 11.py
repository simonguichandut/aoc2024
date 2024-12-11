import sys
import os
from utils import *
from collections import defaultdict
from functools import cache

print(__file__)
input_file = sys.argv[1] if len(sys.argv)>1 else __file__.replace(".py",".ex")
if not os.path.exists(input_file):
    sys.exit(f"{input_file} not found")

##################################################

# dict that stores how many stones there are with a given number
stones =  defaultdict(int)
for num in nums(open(input_file).read()):
    stones[num] += 1

@cache
def process(stone):
    if stone==0:
        return [1]
    ss = str(stone)
    if len(ss)%2 == 0:
        s1 = ss[:int(len(ss)/2)]
        s2 = ss[int(len(ss)/2):]
        return [int(s1), int(s2)]
    return [stone*2024]

i = 0
while True:
    if i==25:
        print("Part 1: ", sum(stones.values()))
    if i==75:
        print("Part 2: ", sum(stones.values()))
        break

    new_stones = defaultdict(int)
    for stone,count in stones.items():
        new_numbers = process(stone)
        for number in new_numbers:
            new_stones[number] += count
    stones = new_stones

    i += 1