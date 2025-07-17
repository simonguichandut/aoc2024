from utils import *
from collections import deque

grid,moves = read().split('\n\n')
grid = grid.split('\n')
grid2 = [line.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.') for line in grid]

# convert to list of characters for easier replacing
grid = [list(line) for line in grid]
grid2 = [list(line) for line in grid2]

moves = moves.replace('\n','')
R,C = len(grid),len(grid[0])

directions = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}

verbose = False

def print_grid(grid):
    print('\n'.join([''.join(line) for line in grid])) 

def solve(grid):

    # starting position
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                r0,c0 = r,c

    for move in moves:

        if verbose:
            print(f"Move {move}:")

        dr,dc = directions[move]
        
        Q = deque([(r0,c0)])
        to_move = set() # no duplicates

        while Q:
            r,c = Q.popleft()
            to_move.add((r,c))

            if grid[r+dr][c+dc] == '#':
                to_move = []
                break

            if grid[r+dr][c+dc] == '.':
                continue

            if grid[r+dr][c+dc] in 'O[]':
                Q.append((r+dr,c+dc))

            if grid[r+dr][c+dc] in '[]' and dc == 0:
                # vertical case need to add other bracket to queue
                if grid[r+dr][c+dc] == '[':
                    Q.append((r+dr, c+dc+1))
                else:
                    Q.append((r+dr, c+dc-1)) 

        # New starting position
        if len(to_move) >= 1:
            r0,c0 = r0+dr, c0+dc

        # Swap elements starting from the end
        to_move = sorted(to_move, reverse=True if dr==-1 or dc==-1 else False)
        for _ in range(len(to_move)):
            r,c = to_move.pop()
            assert grid[r+dr][c+dc] == '.'
            grid[r][c], grid[r+dr][c+dc] = grid[r+dr][c+dc], grid[r][c]

        if verbose:
            print_grid(grid)
            print()

    gps = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] in 'O[':
                gps += 100*r + c

    return gps

print("Part 1: ", solve(grid))
print("Part 2: ", solve(grid2))




### Working first solution for part 1

# def solve_pt1(grid):

#     grid = deepcopy(grid)

#     # starting position
#     for r in range(R):
#         for c in range(C):
#             if grid[r][c] == "@":
#                 rx,cx = r,c

#     for move in moves:

#         if verbose:
#             print(f"Move {move}:")

#         dr,dc = directions[move]
#         rocks = 0
#         r,c = rx,cx

#         while grid[r+dr][c+dc] != '#':
#             r,c = r+dr,c+dc
#             if grid[r][c] == 'O':
#                 rocks += 1

#             else:
#                 assert grid[r][c] == '.', grid[r][c]
#                 break 

#         spaces = abs(r-rx + c-cx) # one of those is zero, only horizontal/vertical movements
    
#         if spaces == 0 or spaces <= rocks: # movement not possible
#             continue

#         assert spaces == rocks+1

#         # move the stuff
#         grid[rx][cx] = '.'
#         rx,cx = rx+dr,cx+dc
#         grid[rx][cx] = '@'
#         for i in range(rocks):
#             grid[rx+(i+1)*dr][cx+(i+1)*dc] = 'O'

#         if verbose:
#             print('\n'.join([''.join(line) for line in grid])) 
#             print()

#     gps = 0
#     for r in range(R):
#         for c in range(C):
#             if grid[r][c] == 'O':
#                 gps += 100*r + c

#     return gps

# print("Part 1: ", solve_pt1(grid))