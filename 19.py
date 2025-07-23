from utils import *
from functools import cache

patterns, designs = read().split('\n\n')
patterns = patterns.split(', ')
designs = designs.split('\n')

@cache
def ways(design):
    if design == '':
        return 1
    n = 0
    for p in patterns:
        if design.startswith(p):
            n += ways(design[len(p):])
    return n

N = [ways(d) for d in designs]
print("Part 1: ", sum(n>0 for n in N))
print("Part 2: ", sum(N))

# Alternative pt1
# @cache
# def possible(design):

#     if design == '' or design in patterns:
#         return True

#     for i in range(1,len(design)):
#         if possible(design[:i]):
#             if possible(design[i:]):
#                 return True

# print("Part 1 :", sum(possible(design) for design in designs))