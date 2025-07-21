from utils import *
from collections import deque

corrupted = [tuple(map(int, line.split(','))) for line in read_lines()]

def print_grid(L, num_corrupted, visited):
    grid = []
    for r in range(L):
        line = ''
        for c in range(L):
            if (c,r) in corrupted[:num_corrupted]:
                line += '#'
            elif (r,c) in visited:
                line += 'O'
            else:
                line += '.'
        grid.append(line)
    print('\n'.join(grid))

def bfs(L, num_corrupted, print_result=False):

    start = (0,0,0)
    Q = deque([start])
    visited = set(start)

    while Q:
        r,c,n = Q.popleft()
        if (r,c) == (L-1,L-1):
            break
        for (dr,dc) in adj4:
            ndr,ndc = r+dr,c+dc
            if ndr<0 or ndr>L-1 or ndc<0 or ndc>L-1: continue
            if (ndc,ndr) in corrupted[:num_corrupted]: continue
            if (ndr,ndc) in visited: continue
            visited.add((ndr,ndc))
            Q.append((ndr,ndc,n+1))

    if print_result:
        print_grid(L, num_corrupted, visited)
                
    if (L-1,L-1) in visited:
        return n
    
print("Part 1: ", bfs(71, 1024))

# part 2 brute force...
for i in range(1023, len(corrupted)):
    print(i, end='\r')
    if not bfs(71,i):
        print("Part 2: ", ','.join(str(a) for a in corrupted[i-1]))
        break

# Test input
#print("Part 1: ", bfs(7, 12))
#for i in range(13, len(corrupted)):
#    if not bfs(7,i):
#        print("Part 2: ", ','.join(str(a) for a in corrupted[i-1]))
#        break