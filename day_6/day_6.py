import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# turn on 0,0 through 999,999
# toggle 0,0 through 999,0
# turn off 499,499 through 500,500
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

LIGHTS = [[False for _ in range(1000)] for _ in range(1000)]

total  = 0

for line in puzzle_input:
    if line.startswith("turn on"):
        m = re.match(r"\D*([\d,]+)\D*([\d,]+)", line)
        first = [int(x) for x in m.groups()[0].split(",")]
        second = [int(x) for x in m.groups()[1].split(",")]
        for x in range(first[0], second[0] + 1):
            for y in range(first[1], second[1] + 1):
                if not LIGHTS[x][y]:
                    total += 1
                LIGHTS[x][y] = True
    elif line.startswith("toggle"):
        m = re.match(r"\D*([\d,]+)\D*([\d,]+)", line)
        first = [int(x) for x in m.groups()[0].split(",")]
        second = [int(x) for x in m.groups()[1].split(",")]
        for x in range(first[0], second[0] + 1):
            for y in range(first[1], second[1] + 1):
                if LIGHTS[x][y]:
                    total -= 1
                else:
                    total += 1
                LIGHTS[x][y] = not LIGHTS[x][y]
    else:
        m = re.match(r"\D*([\d,]+)\D*([\d,]+)", line)
        first = [int(x) for x in m.groups()[0].split(",")]
        second = [int(x) for x in m.groups()[1].split(",")]
        for x in range(first[0], second[0] + 1):
            for y in range(first[1], second[1] + 1):
                if LIGHTS[x][y]:
                    total -= 1
                LIGHTS[x][y] = False

# 569999
print(f"answer = {total}")

# Part 2
LIGHTS = [[0 for _ in range(1000)] for _ in range(1000)]

for line in puzzle_input:
    if line.startswith("turn on"):
        m = re.match(r"\D*([\d,]+)\D*([\d,]+)", line)
        first = [int(x) for x in m.groups()[0].split(",")]
        second = [int(x) for x in m.groups()[1].split(",")]
        for x in range(first[0], second[0] + 1):
            for y in range(first[1], second[1] + 1):
                LIGHTS[x][y] += 1
    elif line.startswith("toggle"):
        m = re.match(r"\D*([\d,]+)\D*([\d,]+)", line)
        first = [int(x) for x in m.groups()[0].split(",")]
        second = [int(x) for x in m.groups()[1].split(",")]
        for x in range(first[0], second[0] + 1):
            for y in range(first[1], second[1] + 1):
                LIGHTS[x][y] += 2
    else:
        m = re.match(r"\D*([\d,]+)\D*([\d,]+)", line)
        first = [int(x) for x in m.groups()[0].split(",")]
        second = [int(x) for x in m.groups()[1].split(",")]
        for x in range(first[0], second[0] + 1):
            for y in range(first[1], second[1] + 1):
                LIGHTS[x][y] -= 1
                LIGHTS[x][y] = 0 if LIGHTS[x][y] < 0 else LIGHTS[x][y]

total = 0
for col in LIGHTS:
    total += sum(col)

# 17836115
print(f"answer = {total}")
