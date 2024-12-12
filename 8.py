from utils import *
from collections import defaultdict

data = read_lines()
R,C = len(data), len(data[0])


antennas = defaultdict(list)
for r in range(R):
    for c in range(C):
        if data[r][c] != '.':
            antennas[data[r][c]].append((r,c))

antinodes1 = set()
antinodes2 = set()
for freq in  antennas:
    for antenna1 in antennas[freq]:
        for antenna2 in antennas[freq]:
            if antenna1 != antenna2:
                (r1,c1),(r2,c2) = antenna1,antenna2
                dr,dc = r2-r1, c2-c1
                ra,ca = r1-dr, c1-dc
                if 0<=ra<R and 0<=ca<C:
                    antinodes1.add((ra,ca))
                ra,ca = r2+dr, c2+dc
                if 0<=ra<R and 0<=ca<C:
                    antinodes1.add((ra,ca))

                # y=mx+b -> c=mr+b, m=dc/dr, b=c1-m*r1
                m = dc/dr
                b = c1-m*r1
                for ra in range(R):
                    ca = round(m*ra + b, 10) # rounding out the float error
                    if 0<=ca<C and ca==int(ca):
                        antinodes2.add((ra,ca))

                assert antenna1 in antinodes2 and antenna2 in antinodes2, (antenna2,freq)

print("Part 1: ", len(antinodes1))
print("Part 2: ", len(antinodes2))

# print
# for r in range(R):
#     s = ''
#     for c in range(C):
#         char = data[r][c]
#         if char in antennas:
#             s += char
#         elif (r,c) in antinodes2:
#             s += '#'
#         else:
#             s += '.'
#     print(s)