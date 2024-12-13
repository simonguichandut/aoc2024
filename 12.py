from utils import *
from collections import defaultdict, deque
from functools import cache

garden = read_lines()
R, C = len(garden), len(garden[0])

# Traverse the whole grid
# If never seen this node before, perform BFS to find the whole region
# Area is just the number of elements in the region, need to calculate perimeter
ans = 0
seen_all = set()
for r in range(R):
    for c in range(C):
        if (r,c) not in seen_all:

            Q = deque()
            Q.append((r,c))
            letter = garden[r][c]
            
            perim = 0
            seen = set()
            while Q:
                r,c = Q.popleft()
                if (r,c) not in seen:
                    seen.add((r,c))
                    for (dr,dc) in adj4:
                        if (r+dr,c+dc) in seen: continue
                        if r+dr in range(R) and c+dc in range(C) and garden[r+dr][c+dc] == letter:
                            Q.append((r+dr,c+dc))
                        else: 
                            perim += 1

            # regions.append(list(seen))
            seen_all |= seen

            # update answer
            print(letter, len(seen), perim)
            ans += len(seen) * perim

print("Part 1: ", ans)
#1432742

# Now just need a function to determine the perimeter
# Actually you can always unfold the perimeter into a rectangle
# except no this doesn't always work if there's holes or concavity
def perim(region):
    rows, cols = [x for x in zip(*region)] # basically a transpose
    height, width = max(rows)-min(rows)+1, max(cols)-min(cols)+1
    return 2*(height+width)


# for region in regions:
#     r0,c0 = region[0]
#     print(garden[r0][c0], len(region), perim(region))
#     # print(len(region))