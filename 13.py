from utils import *
from fractions import Fraction

ans1 = ans2 = 0
for block in read().split('\n\n'):
    lines = block.split('\n')
    A,B,P = nums(lines[0]), nums(lines[1]), nums(lines[2])
    M = [[A[0], B[0]], [A[1], B[1]]]
    V = P
    # Solve MX=V
    (a,b),(c,d) = M
    det = a*d-b*c
    a,b,c,d = d,-b,-c,a # inverse
    x,y = a*V[0]+b*V[1], c*V[0]+d*V[1]
    if x%det==0 and y%det==0 and x/det<=100 and y/det<=100:
        ans1 += 3*int(x/det) + int(y/det)

    V = [V[0]+10000000000000, V[1]+10000000000000]
    x,y = a*V[0]+b*V[1], c*V[0]+d*V[1]
    if x%det==0 and y%det==0:
        ans2 += 3*int(x/det) + int(y/det)

print("Part 1: ", ans1)
print("Part 2: ", ans2)