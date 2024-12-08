import sys
import os
from utils import *

print(__file__)
input_file = sys.argv[1] if len(sys.argv)>1 else __file__.replace(".py",".ex")
if not os.path.exists(input_file):
    sys.exit(f"{input_file} not found")

grid = open(input_file).read().strip().split('\n')
R,C = len(grid),len(grid[0])
##################################################

for r,line in enumerate(grid):
    if '^' in line:
        start = (r,line.index('^'))

def turn_right(dr,dc):
    if dc==0:
        dr2,dc2 = 0,-dr
    elif dr==0:
        dr2,dc2 = dc,0
    return dr2,dc2

def traverse(grid, check_loop=False):
    r,c = start
    dr,dc = -1,0 # start upward
    # unless!
    if grid[r+dr][c+dc]=='#':
        dr,dc = 0,1
    visited = {(r,c,dr,dc)}
    loop = False
    while 0<=r+dr<R and 0<=c+dc<C:
        r,c = r+dr,c+dc

        while 0<=r+dr<R and 0<=c+dc<C and grid[r+dr][c+dc] == '#':  # while not if! might be at a corner and need to turn right twice
            dr,dc = turn_right(dr,dc)

        if (r,c,dr,dc) in visited:
            loop = True
            break
        else:
            visited.add((r,c,dr,dc))

    if check_loop: return loop
    return set((r,c) for r,c,_,_ in visited) # for unique visited nodes, get rid of dr,dc components 

path = traverse(grid)
print("Part 1: ", len(path))

ans2 = 0
# for r in range(R):
#     for c in range(C):
for (r,c) in path: # only need to test locations that are in the initial path, which is a bit faster
    if (r,c)!=start and grid[r][c]!='#':
        grid2 = grid[:]
        grid2[r] = grid2[r][:c] + '#' + grid2[r][c+1:]
        if traverse(grid2, check_loop=True):
            ans2 += 1
        del grid2

print("Part 2: ", ans2)