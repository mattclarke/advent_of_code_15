import json
import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# [
# [1,2,3],
# [1,{"c":"red","b":2},3],
# {"d":"red","e":[1,2,3,4],"f":5},
# [1,"red",5]
# ]
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

total = 0
for line in puzzle_input:
    m = re.findall(r"-?\d+", line)
    for num in m:
        total += int(num)

# 156366
print(f"answer = {total}")

# Part 2
accounts = json.loads(PUZZLE_INPUT)
print(accounts)

total = 0


def solve(structure):
    global total
    if isinstance(structure, dict):
        # Pre-check for "red"
        no_red = True
        for n, v in structure.items():
            if n == "red" or v == "red":
                no_red = False
                break
        if no_red:
            for item in structure.values():
                if isinstance(item, list) or isinstance(item, dict):
                    solve(item)
                elif isinstance(item, int):
                    total += item
    elif isinstance(structure, list):
        for item in structure:
            if isinstance(item, list) or isinstance(item, dict):
                solve(item)
            elif isinstance(item, int):
                total += item
    else:
        assert False


solve(accounts)

# 96852
print(f"answer = {total}")
