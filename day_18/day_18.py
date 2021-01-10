import re
from functools import reduce

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

BOARD = set()

DIMENSION = len(puzzle_input)
assert DIMENSION == len(puzzle_input[0])

for y, line in enumerate(puzzle_input):
    for x, c in enumerate(line):
        if c == "#":
            BOARD.add((y, x))


def tick(board):
    result = set()
    for y in range(0, DIMENSION):
        for x in range(0, DIMENSION):
            neighbours = 0
            for ny, nx in [
                (-1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, -1),
                (-1, -1),
            ]:
                if (y + ny, x + nx) in board:
                    neighbours += 1
            if (y, x) in board and neighbours in [2, 3]:
                result.add((y, x))
            elif (y, x) not in board and neighbours == 3:
                result.add((y, x))
    return result


new_board = BOARD.copy()

for _ in range(100):
    new_board = tick(new_board)

# 768
print(f"answer = {len(new_board)}")

# Part 2
new_board = BOARD.copy()
new_board.add((0, 0))
new_board.add((0, DIMENSION - 1))
new_board.add((DIMENSION - 1, 0))
new_board.add((DIMENSION - 1, DIMENSION - 1))

for _ in range(100):
    new_board = tick(new_board)
    new_board.add((0, 0))
    new_board.add((0, DIMENSION - 1))
    new_board.add((DIMENSION - 1, 0))
    new_board.add((DIMENSION - 1, DIMENSION - 1))

# 781
print(f"answer = {len(new_board)}")
