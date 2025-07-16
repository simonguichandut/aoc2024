from utils import *

data = read_lines()

# w,h = 11,7 # example input
w,h = 101,103 # input

## Part 1
t = 100
top_left, top_right, bot_left, bot_right = 0,0,0,0

for line in data:
    p,v = line.split(' ')
    x0,y0 = list(map(int, p.split('=')[1].split(',')))
    vx,vy = list(map(int, v.split('=')[1].split(',')))

    x = (x0 + vx*t)%w
    y = (y0 + vy*t)%h

    if x<w//2 and y<h//2:
        top_left += 1

    elif x>w//2 and y<h//2:
        top_right += 1

    elif x<w//2 and y>h//2:
        bot_left += 1

    elif x>w//2 and y>h//2:
        bot_right += 1

print("Part 1: ", top_left*top_right*bot_left*bot_right)


## Part 2
t = 0
# while True:
f = open("14_output.txt", 'w')

while t < 10_000:

    robots = set()
    for line in data:
        p,v = line.split(' ')
        x0,y0 = list(map(int, p.split('=')[1].split(',')))
        vx,vy = list(map(int, v.split('=')[1].split(',')))
        x = (x0 + vx*t)%w
        y = (y0 + vy*t)%h
        robots.add((x,y))

    grid = ['-'*w]
    for y in range(h):
        line = '|'
        for x in range(w):
            if (x,y) in robots:
                line += '*'
            else:
                line += ' '
        line += '|'
        grid.append(line)
    grid.append('-'*w)

    # print(f'{t=}')
    # print('\n'.join(grid))
    # os.system('clear')
    f.write(f'{t=}\n')
    f.write('\n'.join(grid))
    f.write('\n')

    t += 1

f.close()

# Part 2 answer: ctrl-f the output file for a long sequence of * '******'