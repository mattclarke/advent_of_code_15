with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# ))(((((
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

puzzle_input = [x for x in puzzle_input[0]]

floor = 0
for p in puzzle_input:
    if p == "(":
        floor += 1
    else:
        floor -= 1

# 280
print(f"answer = {floor}")

# Part 2
floor = 0
for i, p in enumerate(puzzle_input):
    if p == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        # 1797
        print(f"answer = {i + 1}")
        break
