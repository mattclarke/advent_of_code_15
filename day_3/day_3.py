with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# ^v^v^v^v^v
# """

puzzle_input = PUZZLE_INPUT.strip()
print(puzzle_input)

position = [0, 0]

visited = set()
visited.add((position[0], position[1]))

for direction in puzzle_input:
    if direction == ">":
        position[0] += 1
    elif direction == "<":
        position[0] -= 1
    elif direction == "^":
        position[1] += 1
    else:
        position[1] -= 1
    visited.add((position[0], position[1]))

print(f"answer = {len(visited)}")

# Part 2
santa = [0, 0]
robot = [0, 0]

visited = set()
visited.add((santa[0], santa[1]))

for i, direction in enumerate(puzzle_input):
    if i % 2 == 0:
        position = robot
    else:
        position = santa

    if direction == ">":
        position[0] += 1
    elif direction == "<":
        position[0] -= 1
    elif direction == "^":
        position[1] += 1
    else:
        position[1] -= 1
    visited.add((position[0], position[1]))

# 2341
print(f"answer = {len(visited)}")
