import re
from functools import reduce

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# e => H
# e => O
# H => HO
# H => OH
# O => HH
#
# HOHOHO
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

REPLACEMENTS = {}
FORMULA = None

passed_nl = False

for line in puzzle_input:
    if line == "":
        passed_nl = True
        continue

    if passed_nl:
        FORMULA = line
    else:
        name, replacement = line.split(" => ")
        temp = REPLACEMENTS.get(name, [])
        temp.append(replacement)
        REPLACEMENTS[name] = temp

distinct = set()

for n in REPLACEMENTS:
    for r in REPLACEMENTS[n]:
        # TODO: don't need c
        for i, c in enumerate(FORMULA):
            if FORMULA[i: i + len(n)] == n:
                stem = FORMULA[:i]
                rest = FORMULA[i + len(n):]
                new_molecule = "".join([stem, r, rest])
                distinct.add(new_molecule)

# 509
print(f"answer = {len(distinct)}")

# Part 2
roots = {"e"}
count = 0
found = False

# This attempt blows up rapidly
# Alternative ideas
# - start from the answer and go backwards
# - chunk it, i.e. do replacements until the first "char" matches what we want
# then move to the next difference

REVERSED = {}

for k, v in REPLACEMENTS.items():
    for s in v:
        if s in REVERSED:
            # Should be unique
            assert False
        REVERSED[s] = k

# SORTED = sorted(list(REVERSED.keys()), key=len)
# SORTED.reverse()
# print(SORTED)
#
# new_molecule = FORMULA
# i = 0
#
# while True:
#     print("start")
#     bitten = False
#     lowest = 10000000
#     for m in SORTED:
#         if new_molecule[i:].startswith(m):
#             stem = new_molecule[:i]
#             rest = new_molecule[i + len(m):]
#             # if len(m) > len(REVERSED[m]):
#             new_molecule = "".join([stem, REVERSED[m], rest])
#             bitten = True
#             i = len(REVERSED[m])
#             print(new_molecule)
#             break
#         elif m in new_molecule:
#             i = new_molecule.index(m)
#             stem = new_molecule[:i]
#             rest = new_molecule[i + len(m):]
#             # if len(m) > len(REVERSED[m]):
#             new_molecule = "".join([stem, REVERSED[m], rest])
#             bitten = True
#             i = len(REVERSED[m])
#             print(new_molecule)
#             break
#
#
#
#
# while not found:
#     new_roots = set()
#     for root in roots:
#         for base, replacement in REVERSED.items():
#             for i, c in enumerate(root):
#                 if root[i: i + len(base)] == base:
#                     if root[i: i + len(base)] == base:
#                         stem = root[:i]
#                         rest = root[i + len(base):]
#                         new_molecule = "".join([stem, replacement, rest])
#                         if len(new_molecule) <= len(FORMULA):
#                             new_roots.add(new_molecule)
#                         if new_molecule == "e":
#                             found = True
#                             break
#     roots = new_roots
#     print(roots)
#     count += 1


def find_start(molecule):
    count = 0
    for i, c in enumerate(molecule):
        if c == FORMULA[i]:
            count+= 1
            continue
        return count
    return count

longest = 0

while not found:
    new_roots = set()
    for rt in roots:
        for base, replacements in REPLACEMENTS.items():
            for replacement in replacements:
                # TODO: don't need c
                for i, c in enumerate(rt):
                    if rt[i: i + len(base)] == base:
                        stem = rt[:i]
                        rest = rt[i + len(base):]
                        new_molecule = "".join([stem, replacement, rest])
                        if len(new_molecule) <= len(FORMULA):
                            longest = max(longest, find_start(new_molecule))
                            if longest > 0 and new_molecule.startswith(FORMULA[0:longest]):
                                new_roots.add(new_molecule)
                            elif longest == 0:
                                new_roots.add(new_molecule)

                        if new_molecule == FORMULA:
                            found = True
                            break
    roots = new_roots
    print(len(roots), longest)
    # TODO: check the new roots and if any match the start of the string then
    # throw away ones that don't match
    count += 1

print(f"answer = {count}")
