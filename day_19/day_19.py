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
            if FORMULA[i : i + len(n)] == n:
                stem = FORMULA[:i]
                rest = FORMULA[i + len(n) :]
                new_molecule = "".join([stem, r, rest])
                distinct.add(new_molecule)

# 509
print(f"answer = {len(distinct)}")

# Part 2
roots = {"e"}
count = 0
found = False

# Test target
target = "CaCaSiRnFYSiThCaRnFArAr"
target = FORMULA


# Change from string of elements into a list
def break_down_formula(formula):
    result = []
    while formula:
        elem = (
            formula[0:2] if len(formula) >= 2 and formula[1].islower() else formula[0]
        )
        result.append(elem)
        formula = formula[len(elem):]
    return result


# Simplify by replacing two letter elements with one char
SIMPLIFIED = {
    "Rn": "(",
    "Y": "|",
    "Ar": ")",
    "C": "Z",
}

index = ord("A")

for k in REPLACEMENTS.keys():
    rep = chr(index)
    SIMPLIFIED[k] = chr(index)
    index += 1

bdt = break_down_formula(target)
target = ""

for k in bdt:
    target += SIMPLIFIED[k]
print(target)


REVERSED_RECIPES = {}

for k, v in REPLACEMENTS.items():
    for i in v:
        rep = break_down_formula(i)
        converted = ""
        for c in rep:
            converted += SIMPLIFIED[c]
        REVERSED_RECIPES[converted] = SIMPLIFIED[k]
print(REVERSED_RECIPES)


def solve(formula):
    def _replace(formula, count):
        import re

        two_elements_together = r"[A-Z][A-Z]"
        two_elements_then_open_bracket = r"[A-Z][A-Z]\("
        one_element_in_brackets = r"[A-Z]\([A-Z]\)"
        two_element_then_closing_bracket = r"[A-Z][A-Z]\)"
        two_elements_in_bracket = r"[A-Z]\([A-Z]\|[A-Z]\)"
        three_elements_in_bracket = r"[A-Z]\([A-Z]\|[A-Z]\|[A-Z]\)"
        swap_with = None

        # It is important that this regexes are run in the right order
        for reg in [three_elements_in_bracket, two_elements_in_bracket,
                    one_element_in_brackets,
                    two_element_then_closing_bracket,
                    two_elements_then_open_bracket, two_elements_together]:
            temp_formula = formula
            while m := re.search(reg, temp_formula):
                string = temp_formula[m.regs[0][0]:m.regs[0][1]]
                if string in REVERSED_RECIPES:
                    swap_with = (string, REVERSED_RECIPES[string])
                    break
                else:
                    if string.endswith(")") or string.endswith("("):
                        if string[0:-1] in REVERSED_RECIPES:
                            swap_with = (string, REVERSED_RECIPES[string[0:-1]] + string[~0])
                            break
                temp_formula = temp_formula[m.regs[0][0] + 1:]
            if swap_with:
                break

        if swap_with:
            prefix = formula[0:formula.index(swap_with[0])]
            suffix = formula[formula.index(swap_with[0]) + len(swap_with[0]):]
            formula = prefix + swap_with[1] + suffix
            count += 1

        return formula, count

    count = 0
    while True:
        formula, count = _replace(formula, count)
        print(formula)
        if formula == SIMPLIFIED["e"]:
            # 195
            print(f"answer = {count}")
            break


solve(target)


# Solution from the web = 195
breakdown = break_down_formula(target)
# Every pair reduces down to one element (e.g. ABC => DE => F), for n elements (excluding non-reducibles) = n - 1
# Non-reducibles are in form of A(B) or A(B|C) or A(B|C|D)
# A(B) gets swallowed as one move, so -1 for the '(' and the ')'
# A(B|C) same as previous but another -1 for the the '|'
# A(B|C|D) same as previous but another -1 for the extra '|'
# NOTE: assumes the formula is solvable!
total = len(breakdown) - 1 - breakdown.count("(") - breakdown.count(")") - 2 * breakdown.count("|")
print(f"answer = {total}")
