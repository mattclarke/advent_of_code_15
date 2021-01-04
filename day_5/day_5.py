import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# ugknbfddgicrmopn
# aaa
# jchzalrnumimnmhp
# haegwjzuvuyypxyu
# dvszwmarrgswjxmb
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

nice = 0

for line in puzzle_input:
    # Can we regex this line?
    ans_r1 = len([x for x in line if x in ["a", "e", "i", "o", "u"]]) >= 3
    if not ans_r1:
        # print(f"r1 failed for {line}")
        continue

    # Use back reference to see if char repeated
    ans_r2 = re.search(r"(.)\1+", line)
    if not ans_r2:
        # print(f"r2 failed for {line}")
        continue

    # Check for disallowed pairs
    ans_r3 = re.search(r"ab|cd|pq|xy", line)
    if ans_r3:
        # print(f"r3 failed for {line}")
        continue
    nice += 1


# 255
print(f"answer = {nice}")


# Part 2
# PUZZLE_INPUT = """
# qjhvhtzxzqqjkmpb
# xxyxx
# uurcxstgmygtbstg
# ieodomkazucvgmuy
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")

nice = 0

for line in puzzle_input:
    ans_r1 = False
    for i in range(len(line) - 1):
        target = line[i : i + 2]
        for j in range(i + 2, len(line) - 1):
            if line[j : j + 2] == target:
                ans_r1 = True
                break
        if ans_r1:
            break
    if not ans_r1:
        # print(f"r1 failed for {line}")
        continue

    ans_r2 = [True for i in range(len(line) - 2) if line[i] == line[i + 2]]
    if not ans_r2:
        # print(f"r2 failed for {line}")
        continue
    nice += 1

# 55
print(f"answer = {nice}")
