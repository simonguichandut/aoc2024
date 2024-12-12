from utils import *

data = read_lines()
R,C = len(data), len(data[0])

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