import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = r"""
# ""
# "abc"
# "aaa\"aaa"
# "\x27"
# "njro\x68qgbx\xe4af\"\\suan"
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

total = 0

for line in puzzle_input:
    num_chars = len(line)
    line = line.strip('"')
    num = len(line)
    num -= len(re.findall(r'\\"', line))
    num -= 3 * len(re.findall(r"\\x[\dabcdef]{2}", line))
    num -= len(re.findall(r"\\\\", line))
    total += num_chars - num

# 1350
print(f"answer = {total}")

# Part 2
total = 0

for line in puzzle_input:
    num_chars = len(line)
    line = line.replace("\\", "\\\\")
    line = line.replace('"', '\\"')

    num = len(line) + 2  # The extra surrounding quotes
    total += num - num_chars
    print(f"{line}", num, num_chars)

# 2085
print(f"answer = {total}")
