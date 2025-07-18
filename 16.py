from utils import *
from collections import defaultdict
import heapq

grid = read_lines()

R,C = len(grid), len(grid[0])
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S':
            break
    else:
        continue
    break

# Dijkstra using priority queue
# first item in the tuple is the distance which the queue prioritizes

node = (r,c)
direction = (0,1)
score = 0
path = [(r,c)]

queue = [(score,node,direction,path)]
heapq.heapify(queue)

node_scores = defaultdict(lambda: 1e10) # this replaces the usual visited set. We CAN visit a node more than once to solve pt2
all_paths = defaultdict(set) # key is score, value is the set of nodes 

while queue:

    score,node,direction,path = heapq.heappop(queue)

    if score > node_scores[(node, direction)]:
        continue
    node_scores[(node, direction)] = score

    r,c = node
    
    if grid[r][c] == 'E':
        all_paths[score] |= set(path) # this adds new nodes which are also part of a path with the same score
        # break
        continue

    for (dr,dc) in adj4:

        # can't turn 180
        if dr*direction[0] + dc*direction[1] == -1:
            continue

        if r+dr<0 or r+dr>=R or c+dc<0 or c+dc>=C:
            continue

        if grid[r+dr][c+dc] == '#':
            continue

        turn_cost = 0
        if (dr,dc) != direction:
            turn_cost = 1000

        heapq.heappush(queue, 
                       (score + 1 +turn_cost,  # new score
                        (r+dr, c+dc),          # new position
                        (dr, dc),              # new direction
                        path + [(r+dr,c+dc)])  # update path
                    )

best_score = min(all_paths.keys())
print("Part 1: ", best_score)
print("Part 2: ", len(all_paths[best_score]))

# # print the best paths
# print('\n'.join([''.join(['O' if (r,c) in all_paths[best_score] else grid[r][c] for c in range(C)]) for r in range(R)]))