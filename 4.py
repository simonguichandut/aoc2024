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

# First try for part 1, it works but it's no longer useful in part 2

# # right/left
# for i in range(R):
#     row = data[i]
#     ans += row.count('XMAS') + row.count('SAMX')
# # up/down
# for j in range(C):
#     col = ''.join([data[i][j] for i in range(R)])
#     ans += col.count('XMAS') + col.count('SAMX')

# # diagonals
# # corner notation: #1=North East, #2=NW, #3=SW, #4=SE

# # NW-SE diagonals
# # Starting point starting from 3 to 1, going through 2
# start_row = list(range(R-1,-1,-1)) + [0 for _ in range(C-1)]
# start_col = [0 for _ in range(R-1)] + list(range(0,C))
# for r,c in zip(start_row,start_col):
#     diag = ''
#     while r<R and c<C:
#         diag += data[r][c]
#         r += 1
#         c += 1 
#     ans += diag.count('XMAS') + diag.count('SAMX')

# # SW-NE diagonals
# # Starting point starting from 2 to 4, going through 3
# start_row = list(range(R)) + [R-1 for _ in range(C-1)]
# start_col = [0 for _ in range(R-1)] + list(range(0,C))
# for r,c in zip(start_row,start_col):
#     diag = ''
#     while r>=0 and c<C:
#         diag += data[r][c]
#         r -= 1
#         c += 1 
#     ans += diag.count('XMAS') + diag.count('SAMX')

# create padded grid of characters to avoid out of bounds
# method put into utils
grid = pad(data, 4)
ans1 = ans2 = 0
for i in range(4,4+R):
    for j in range(4,4+C):
        if grid[i][j] == 'X':
            if grid[i][j:j+4] == 'XMAS': # right
                ans1+=1
            if grid[i][j-3:j+1] == 'SAMX': # left
                ans1+=1
            if ''.join(grid[ii][j] for ii in range(i,i+4)) == 'XMAS': # down
                ans1+=1
            if ''.join(grid[ii][j] for ii in range(i,i-4,-1)) == 'XMAS': # up
                ans1+=1
            if ''.join(grid[ii][jj] for ii,jj in zip(range(i,i+4),range(j,j+4))) == 'XMAS': # south east
                ans1+=1
            if ''.join(grid[ii][jj] for ii,jj in zip(range(i,i+4),range(j,j-4,-1))) == 'XMAS': # south west
                ans1+=1
            if ''.join(grid[ii][jj] for ii,jj in zip(range(i,i-4,-1),range(j,j+4))) == 'XMAS': # north east
                ans1+=1
            if ''.join(grid[ii][jj] for ii,jj in zip(range(i,i-4,-1),range(j,j-4,-1))) == 'XMAS': # north west
                ans1+=1

        if grid[i][j] == 'A':
            if ''.join(grid[ii][jj] for ii,jj in zip(range(i-1,i+2),range(j-1,j+2))) in ('MAS','SAM') and\
               ''.join(grid[ii][jj] for ii,jj in zip(range(i-1,i+2),range(j+1,j-2,-1))) in ('MAS','SAM'):
                ans2+=1

print("Part 1: ",ans1)
print("Part 2: ",ans2)



