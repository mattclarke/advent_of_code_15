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
            if index > 200:
                print(index, r)
            # print("current", elem, r)
            expand = break_down_formula(r)
            prefix = so_far[:index]
            suffix = so_far[index + 1:]
            if expand[0] == target[index]:
                _solve(prefix + expand + suffix, index + 1)

            # Evolve the first element
            # TODO: stop this recusing off forever
            # TODO: Should we always do this even if the current elem matches the target?

            # SPIKE: ignore Ca => CaF style for now as need to work out how to handle those
            # And P => BP
            # if expand == prev:
            #     continue
            #
            # if len(prefix + expand + suffix) < len(target):
            #     _solve(prefix + expand + suffix, index, expand)
            # else:
            #     return


    _solve(incoming, 0, [])


for x in REPLACEMENTS["e"]:
    print(x)
    solve(break_down_formula(x), break_down_formula(target))



# def find_where_diverge(a, b):
#     index = 0
#     for i, j in zip(a, b):
#         if i != j:
#             if i.islower() or j.islower():
#                 index -= 1
#             break
#         index += 1
#     return index
#
#
# assert find_where_diverge("CF", "CF") == 2
# assert find_where_diverge("CFG", "CFG") == 3
# assert find_where_diverge("CFG", "CFX") == 2
# assert find_where_diverge("A", "B") == 0
# assert find_where_diverge("ACa", "ACb") == 1
# assert find_where_diverge("Ca", "Cb") == 0
# assert find_where_diverge("C", "") == 0
# assert find_where_diverge("", "A") == 0
#
# possibles = {}
#
#
# def find_poss(molecule, seen):
#     if molecule not in REPLACEMENTS:
#         return
#
#     for poss in REPLACEMENTS[molecule]:
#         front = poss[0:2] if len(poss) > 1 and poss[1].islower() else poss[0]
#         if front in seen:
#             continue
#         seen.add(front)
#         find_poss(front, seen)
#
#
# for k in REPLACEMENTS:
#     poss = set()
#     find_poss(k, poss)
#     possibles[k] = poss
#
#
# def solve(current: str, target: str):
#     best = [10000000000000]
#     dead_ends = set()
#
#     def _solve(current, target, count, depth=0):
#         if len(current) > len(target) or count >= best[0]:
#             return False
#         if current == target:
#             print("SOLVED", count, depth)
#             best[0] = count
#             return True
#
#         front = get_front(current)
#         front_t = get_front(target)
#         if front not in REPLACEMENTS:
#             return False
#         for option in REPLACEMENTS[front]:
#             new_molecule = option + current[len(front):]
#
#             index = find_where_diverge(new_molecule, target)
#             if index > 0:
#                 print(depth, count + 1, len(new_molecule[index:]))
#                 res = _solve(new_molecule[index:], target[index:], count+1, depth + 1)
#                 # print("OUT")
#
#             # If there is no way to get to the target's first molecule then skip
#             front_opt = get_front(new_molecule)
#             if front_opt not in possibles or front_t not in possibles[front_opt]:
#                 continue
#
#             # print(new_molecule)
#             _solve(new_molecule, target, count + 1)
#
#     def get_front(current):
#         return current[0:2] if len(current) > 1 and current[1].islower() else current[0]
#
#     _solve(current, target, 0)
#
# solve("e", target)
