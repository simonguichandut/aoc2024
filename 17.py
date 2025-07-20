from utils import *

registers, program = read().split('\n\n')
A,B,C = (int(reg.split(': ')[1]) for reg in registers.split('\n'))
program = list(map(int, program.split(': ')[1].split(',')))

def run_program(program: list, A:int, B:int, C:int):

    i = 0
    while i < len(program):

        code, op = program[i:i+2]

        match op:
            case 4: opc = A
            case 5: opc = B
            case 6: opc = C
            case 7: raise op
            case _: opc = op
        # op is the literal operand, opc is the combo

        match code:
            case 0: A = int(A//2**opc)   # adv
            case 1: B = B^op             # bxl
            case 2: B = opc%8            # bst
            case 3:                      # jnz
                if A != 0:
                    i = op
                    continue
            case 4: B = B^C              # bxc
            case 5: yield opc%8          # out - This function is a generator!
            case 6: B = int(A//2**opc)   # adv
            case 7: C = int(A//2**opc)   # adv

        i += 2
        # print(A)

print("Part 1: ", ','.join(str(x) for x in run_program(program,A,B,C)))


# Part 2
# Approach: find out which number (<8) is needed to print out the final
# number in the program. There are only prints for register A, and A only changes
# by dividing itself by 8. Therefore, once we get that number, multiplying it by 8
# doesn't change the output. From there, we increment by 1 to 8 to find what is need
# output the last 2 numbers of the program (including the one we had before), and so on
# until we are able to print out the whole program. Need to backtrack sometimes, 
# which is implemented crudely..

check_index = len(program)-1
A = 0
A_bad = []
while check_index >= 0:
    success = False
    for i in range(8):
        if (A+i)*8 not in A_bad:
            output = list(run_program(program,A+i,0,0))
            if output == program[check_index:]:  # comparing the final (len(program)-check_index) numbers
                success = True
                break
    if success:
        A += i
        if check_index == 0: # finished
            break
        A *= 8
        check_index -= 1
    else:
        # Need to backtrack here
        A_bad.append(A)
        A = int(A/8)
        check_index += 1

assert program == list(run_program(program,A,0,0))
print("Part 2: ", A)