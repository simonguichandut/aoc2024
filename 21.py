# Solution inspired by HyperNeutrino
# https://www.youtube.com/watch?v=dqzAaj589cM

from utils import *
from collections import defaultdict, deque
from functools import cache
import itertools

codes = read_lines()

def get_sequences(keypad):
    """
    Compute all the possible shortest length sequences of moves to get from one key to another (and press the second one).
    Returns a dictionary where the key is the a (start,end) tuple and the value is a list of sequences.
    A sequence is a string such as '^>>vA'
    """

    pos = {} # positions of all keys
    for r in range(len(keypad)):
        for c in range(len(keypad[0])):
            if keypad[r][c] is not None: pos[keypad[r][c]] = (r,c)

    # BFS for each pair of keys
    sequences = defaultdict(list)
    for x in pos:
        for y in pos:
            if x==y: # same key, just need to press A
                sequences[(x,y)].append('A')
                continue

            q = deque([(pos[x], '')]) # second item is the current sequence of moves
            optimal = float('inf')

            while q:
                (r,c), moves = q.popleft()

                if keypad[r][c] == y:
                    if len(moves)+1 > optimal: break # once we are looking at non-optimal paths we are done
                    optimal = len(moves) + 1
                    sequences[(x,y)].append(moves + 'A')

                for nr,nc,move in [(r-1,c,'^'), (r+1,c,'v'), (r,c-1,'<'), (r,c+1,'>')]:
                    if nr<0 or nr>=len(keypad) or nc<0 or nc>=len(keypad[0]): continue
                    if keypad[nr][nc] is None: continue
                    q.append(((nr,nc), moves + move))

    return sequences


num_sequences = get_sequences([['7','8','9'],
                               ['4','5','6'],
                               ['1','2','3'],
                               [None,'0','A']])

dir_sequences = get_sequences([[None,'^','A'],
                               ['<','v','>']])

@cache
def sequence_length(seq, depth=1):
    # Compute the length of the move sequence to make depending on the depth (number of robots on dir keypads)

    # base case is depth 1, the first robot on a dir keypad
    # the total length is the sum of lengths of sequences between each pair of characters
    if depth == 1:
        return sum(len(dir_sequences[(a,b)][0]) for a,b in zip('A'+seq, seq))

    # Otherwise, recurse
    length = 0
    for a,b in zip('A'+seq, seq):
        length += min(sequence_length(subseq, depth-1) for subseq in dir_sequences[(a,b)])
    return length

def solve(depth=2):
    complexity = 0
    for code in codes:
        inputs = [num_sequences[(a,b)] for a,b in zip('A'+code, code)] # all possible sequences on the initial keypad
        inputs = [''.join(x) for x in itertools.product(*inputs)]
        length = min(sequence_length(input, depth) for input in inputs)
        #print(code, length)
        complexity += int(code[:-1])*length
    return complexity

print("Part 1: ", solve())
print("Part 1: ", solve(depth=25))