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
        formula = formula[len(elem) :]
    return result


target = target.replace("Rn", "(").replace("Y", "|").replace("Ar", ")")
print(target)


REVERSED_RECIPES = {}

for k, v in REPLACEMENTS.items():
    for i in v:
        assert i not in REVERSED_RECIPES
        REVERSED_RECIPES[i.replace("Rn", "(").replace("Y", "|").replace("Ar", ")")] = k
print(REVERSED_RECIPES)


def solve(formula):
    def _replace(formula, count):
        import re

        two_elements_together = "[A-Z][a-z]?[A-Z][a-z]?"
        two_elements_then_open_bracket = "[A-Z][a-z]?[A-Z][a-z]?\("
        one_element_in_brackets = "[A-Z][a-z]?\([A-Z][a-z]?\)"
        two_element_then_closing_bracket = "[A-Z][a-z]?[A-Z][a-z]?\)"
        two_elements_in_bracket = "[A-Z][a-z]?\([A-Z][a-z]?\|[A-Z][a-z]?\)"
        three_elements_in_bracket = "[A-Z][a-z]?\([A-Z][a-z]?\|[A-Z][a-z]?\|[A-Z][a-z]?\)"

        replacement = None

        for reg in [three_elements_in_bracket, two_elements_in_bracket, one_element_in_brackets,
                    two_element_then_closing_bracket, two_elements_then_open_bracket, two_elements_together]:
            m = re.search(reg, formula)
            temp = formula
            while m:
                string = temp[m.regs[0][0]:m.regs[0][1]]
                if string in REVERSED_RECIPES:
                    replacement = (string, REVERSED_RECIPES[string])
                    break
                else:
                    if string.endswith(")") or string.endswith("("):
                        if string[0:-1] in REVERSED_RECIPES:
                            replacement = (string, REVERSED_RECIPES[string[0:-1]] + string[~0])
                            break
                temp = temp[m.regs[0][0] + 1:]
                m = re.search(
                    reg,
                    temp)
            if replacement:
                break

        if replacement:
            print(replacement[0], replacement[1])
            formula = formula.replace(replacement[0], replacement[1])
            count += 1

        return formula, count

    count = 0
    while True:
        formula, count = _replace(formula, count)
        print(">>>", formula)
        if formula == "e":
            # Currently count is two low, should be 195
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
total = len(breakdown) - 1 - breakdown.count("(") - breakdown.count(")") - 2 * breakdown.count("|")
