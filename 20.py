from utils import *
from collections import defaultdict

grid = read().split('\n')
R,C = len(grid),len(grid[0])
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S': S = (r,c)
        if grid[r][c] == 'E': E = (r,c)

distances = {E:0}
r,c = E
while (r,c) != S:
    for dr,dc in adj4:
        if grid[r+dr][c+dc] != '#' and (r+dr,c+dc) not in distances:
            distances[(r+dr,c+dc)] = distances[(r,c)] + 1
            r,c = r+dr,c+dc
            break
#print(distances[S])

def cheat_saves(max_cheat):
    Saves = defaultdict(int)
    for (r,c) in distances:
        for rc in range(R):
            for cc in range(C):
                if (rc,cc) not in distances: continue
                dist_cheat = abs(rc-r) + abs(cc-c)
                if dist_cheat > max_cheat: continue # manhattan distance
                dist = distances[(rc,cc)] + dist_cheat + (distances[S]-distances[(r,c)])
                save = distances[S] - dist
                Saves[save] += 1
    return Saves

Saves2 = cheat_saves(2)
Saves20 = cheat_saves(20)
print("Part 1: ", sum(Saves2[save] for save in Saves2 if save>=100))
print("Part 2: ", sum(Saves20[save] for save in Saves20 if save>=100))

# Testing
# print('\n'.join([f"{y} that save {x}" for x,y in sorted(Saves2.items()) if x>0]))
# print('\n'.join([f"{y} that save {x}" for x,y in sorted(Saves20.items()) if x>=50]))