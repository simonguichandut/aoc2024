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

for line in  data:
    print(line)

# print("Part 1: ",)
# print("Part 2: ",)



