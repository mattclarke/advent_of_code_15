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

# Test target
target = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSi"
target = FORMULA


# Change from string of elements into a list
def break_down_formula(formula):
    result = []
    while formula:
        elem = formula[0:2] if len(formula) >= 2 and formula[1].islower() else \
        formula[0]
        result.append(elem)
        formula = formula[len(elem):]
    return result


# Work out for each element what other elements it can change to (ignoring
# the trailing elements)
POSSIBILITIES = {}
CHOICES = {}

for k in REPLACEMENTS.keys():
    possiblities = set()
    choices = set()
    tracker = set()
    starts = REPLACEMENTS[k]
    choices |= set(starts)
    while starts:
        new_starts = []
        for x in starts:
            elem = x[0:2] if len(x) >=2 and x[1].islower() else x[0]
            rest = x[len(elem):]

            # if elem not in possiblities:
            possiblities.add(elem)
            if elem in REPLACEMENTS:
                for i in REPLACEMENTS[elem]:
                    temp = i + rest
                    if temp not in choices:
                        if i not in tracker:
                            new_starts.append(temp)
                        tracker.add(i)
                        choices.add(temp)
        starts = new_starts
    POSSIBILITIES[k] = possiblities
    CHOICES[k] = choices

print(POSSIBILITIES)
print(CHOICES)

MAX = 0

def solve(incoming, target):
    failures_by_index = {}

    def _solve(so_far, index, prev=[]):
        global MAX

        elem = so_far[index]
        if index > MAX:
            MAX = index
            print(MAX)

        if so_far == target:
            print("Halt")
            raise Exception(MAX)

        if index >= len(target):
            print("Too long")
            return

        # print("\n", "".join(so_far[:index]), "".join(so_far[index:]))
        # print("", "".join(target[:index]), "".join(target[index:]))
        if index in failures_by_index and elem in failures_by_index[index]:
            return
        # print(elem)
        if elem not in REPLACEMENTS:
            # It is an element that we cannot transform
            # If it matches then skip it
            if elem == target[index]:
                _solve(so_far, index + 1)
                # Cannot do anything further with it
                return
            else:
                # No good
                f = failures_by_index.get(index, set())
                f.add(elem)
                failures_by_index[index] = f
                # print("Deadend 1")
                return

        # Check already matched
        if target[index] == elem:
            _solve(so_far, index + 1)
        elif not target[index] in POSSIBILITIES[elem]:
            f = failures_by_index.get(index, set())
            f.add(elem)
            failures_by_index[index] = f
            # print("Deadend 2")
            return
        for r in CHOICES[elem]:
            if index >= 224:
                print(index, r, "".join(so_far))
                # print("".join(target))
                # raise Exception("Oops")
            # print("current", elem, r)
            expand = break_down_formula(r)
            prefix = so_far[:index]
            suffix = so_far[index + 1:]
            if expand[0] == target[index]:
                _solve(prefix + expand + suffix, index + 1)
