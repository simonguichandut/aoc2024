from utils import *
from collections import defaultdict, deque              
from functools import cache

garden = read_lines()
R, C = len(garden), len(garden[0])     
                                                                         
# Traverse the whole grid                               
# If never seen this node before, perform BFS to find the whole region                                      
# Area is just the number of elements in the region. Add one to perimeter every time a neighbour is not part of the region.

# hyperneutrino's corner method for pt2
def sides(region):
    corner_coords = set()
    for (r,c) in region:
        for rr,cc in [(r-0.5, c+0.5), (r+0.5, c+0.5), (r+0.5, c-0.5), (r-0.5, c-0.5)]:
            corner_coords.add((rr,cc))
    num_sides = 0
    for rr,cc in corner_coords:
        config = [(r,c) in region for (r,c) in [(rr-0.5, cc+0.5), (rr+0.5, cc+0.5), (rr+0.5, cc-0.5), (rr-0.5, cc-0.5)]]
        match sum(config):
            case 1:
                num_sides += 1
            case 2:
                if config == [True, False, True, False] or config == [False, True, False, True]:
                    num_sides += 2
            case 3:
                num_sides += 1
    return num_sides

ans1 = ans2 = 0
seen = set()
for r in range(R):                                          
    for c in range(C):
        if (r,c) not in seen:
              
            Q = deque()                                             
            Q.append((r,c))
            letter = garden[r][c]                       
            perim = 0
            region = set()
            while Q:
                rr,cc = Q.popleft()
                if (rr,cc) not in region:
                    region.add((rr,cc))
                    for (dr,dc) in adj4:
                        if (rr+dr,cc+dc) in region: continue
                        if rr+dr in range(R) and cc+dc in range(C) and garden[rr+dr][cc+dc] == letter:
                            Q.append((rr+dr,cc+dc))
                        else:
                            perim += 1

            ans1 += len(region) * perim
            ans2 += len(region) * sides(region)
            seen |= region

print("Part 1: ", ans1)
print("Part 2: ", ans2)