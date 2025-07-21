from utils import *
from collections import deque,defaultdict

corrupted = [tuple(map(int, line.split(','))) for line in read_lines()]

def print_grid(L, num_corrupted, marked):
    grid = []
    for r in range(L):
        line = ''
        for c in range(L):
            if (c,r) in corrupted[:num_corrupted]:
                line += '#'
            elif (r,c) in marked:
                line += 'O'
            else:
                line += '.'
        grid.append(line)
    print('\n'.join(grid))

def bfs(L, num_corrupted, print_result=False):

    start = (0,0)
    Q = deque([start])
    visited = set(start)
    parents = defaultdict(None)

    while Q:
        r,c = Q.popleft()
        if (r,c) == (L-1,L-1):
            break
        for (dr,dc) in adj4:
            ndr,ndc = r+dr,c+dc
            if ndr<0 or ndr>L-1 or ndc<0 or ndc>L-1: continue
            if (ndc,ndr) in corrupted[:num_corrupted]: continue
            if (ndr,ndc) in visited: continue
            visited.add((ndr,ndc))
            parents[(ndr,ndc)] = (r,c)
            Q.append((ndr,ndc))
                
    if (L-1,L-1) in visited:
        curr = (L-1,L-1)
        shortest = [curr]
        while parents[curr]:
            curr = parents[curr]
            if curr == start:
                break
            shortest.append(curr)

        if print_result:
            print_grid(L, num_corrupted, shortest)

        return shortest

shortest = bfs(71, 1024)
print("Part 1: ", len(shortest))

for i in range(1023, len(corrupted)):
    print(i, end='\r')
    if corrupted[i-1][::-1] not in shortest:
        continue
    shortest = bfs(71,i)
    if shortest is None:
        print("Part 2: ", ','.join(str(a) for a in corrupted[i-1]))
        break

# Test input
# shortest = bfs(7, 12)
# print("Part 1: ", len(shortest))

# for i in range(13, len(corrupted)):
#     print(i, end='\r')
#     if corrupted[i-1][::-1] not in shortest:
#         continue
#     shortest = bfs(7,i)
#     if shortest is None:
#         print("Part 2: ", ','.join(str(a) for a in corrupted[i-1]))
#         break