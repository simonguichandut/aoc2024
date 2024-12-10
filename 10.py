import sys
import os
from utils import *

print(__file__)
input_file = sys.argv[1] if len(sys.argv)>1 else __file__.replace(".py",".ex")
if not os.path.exists(input_file):
    sys.exit(f"{input_file} not found")

data = open(input_file).read().strip().split('\n')
R,C = len(data),len(data[0])
##################################################
grid = [[int(c) for c in line] for line in data]

heads = []
for r in range(R):
    for c in range(C):
        if grid[r][c] == 0: heads.append((r,c))

def dfs(node, visited=None, score=None, pt2=False):

    if visited==None: # and paths
        # For some reason it doesn't work to set these as the default arguments to the function
        # It won't re-initialize as the defaults on successive calls
        visited = set()
        score = 0

    visited.add(node)
    r,c = node

    if grid[r][c] == 9:
        score += 1

    else:
        for (dr,dc) in ((1,0),(-1,0),(0,1),(0,-1)):
            if r+dr in range(R) and c+dc in range(C) and grid[r+dr][c+dc]-grid[r][c]==1 and (r+dr,c+dc) not in visited:
                score = dfs(((r+dr),(c+dc)), visited, score, pt2)
    
    if pt2:
        visited.remove(node)

    return score

print("Part 1: ", sum(dfs(head) for head in heads))
print("Part 2: ", sum(dfs(head, pt2=True) for head in heads))