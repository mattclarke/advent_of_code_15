import re
from functools import reduce

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# inc a
# jio a, +2
# tpl a
# inc a
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")

COMMANDS = []
for line in puzzle_input:
    pars = line.replace(",", "").split(" ")
    COMMANDS.append(tuple(pars))
# print(COMMANDS)


def hlf(reg, registers, sp):
    registers[reg] //= 2
    return registers, sp + 1


def tpl(reg, registers, sp):
    registers[reg] *= 3
    return registers, sp + 1


def inc(reg, registers, sp):
    registers[reg] += 1
    return registers, sp + 1


def jmp(value, registers, sp):
    value = int(value)
    return registers, sp + value


def jie(reg, value, registers, sp):
    if registers[reg] % 2 != 0:
        return registers, sp + 1
    value = int(value)
    return registers, sp + value


def jio(reg, value, registers, sp):
    if registers[reg] != 1:
        return registers, sp + 1
    value = int(value)
    return registers, sp + value


registers = {
    "a": 0,
    "b": 0,
}


def run(registers):
    sp = 0

    while sp < len(COMMANDS):
        cmd = COMMANDS[sp]
        if cmd[0] == "hlf":
            registers, sp = hlf(cmd[1], registers, sp)
        elif cmd[0] == "tpl":
            registers, sp = tpl(cmd[1], registers, sp)
        elif cmd[0] == "inc":
            registers, sp = inc(cmd[1], registers, sp)
        elif  cmd[0] == "jmp":
            registers, sp = jmp(cmd[1], registers, sp)
        elif cmd[0] == "jie":
            registers, sp = jie(cmd[1], cmd[2], registers, sp)
        elif cmd[0] == "jio":
            registers, sp = jio(cmd[1], cmd[2], registers, sp)


# Part 1
registers_1 = dict(registers)
run(registers_1)

# 255
print(f"answer = {registers_1['b']}")

# Part 2
registers_2 = dict(registers)
registers_2["a"] = 1
run(registers_2)

# 334
print(f"answer = {registers_2['b']}")


