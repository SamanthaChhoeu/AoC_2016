#!/usr/bin/python
# test... python solution.py < input.txt
# NOTE: THIS TAKES 3 MINS TO EXECUTE BECAUSE I'M
# INEFFICIENT AF
import sys,re
pc = 0            # initialise program counter
instructions = [] # stores instructions
registers = {'a': 0,'b': 0,'c': 0,'d': 0}
# check if register or integer
# return int (value in register or int)
def readx(x):
    if x.isalpha():
        return int(registers[x])
    # x is integer
    else:
        return int(x)
# read each line
for line in sys.stdin:
    line = re.sub(r'\n$',"",line) # remove new line
    line = re.sub(r'\s*$',"",line) # remove trailing space
    command = line.split(" ")
    instructions.append(command)

while 1:
    if pc >= len(instructions): # reach end of pc
        break
    command = instructions[pc]
    #print pc,command
    # cpy x y copies x (either an integer or the value of a register) into register y.
    if command[0] == "cpy":
        x = command[1]
        y = command[2]
        registers[y] = readx(x)
    # inc x increases the value of register x by one.
    elif command[0] == "inc":
        x = command[1]
        registers[x] = int(registers[x])+1
    # dec x decreases the value of register x by one.
    elif command[0] == "dec":
        x = command[1]
        registers[x] = int(registers[x])-1
    # jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
    elif command[0] == "jnz":
        x = command[1]
        y = command[2]
        # x not equal 0
        if readx(x) != 0:
            pc += readx(y)
            pc -= 1
    pc += 1
print registers
