import re
from functools import reduce

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

INGREDIENTS = {}

for line in puzzle_input:
    matches = re.match(
        r"^(\w+):[\s\w]+(-?\d+)[,\s\w]+(-?\d+)[,\s\w]+(-?\d+)[,\s\w]+(-?\d+)[,\s\w]+(-?\d+)",
        line,
    )
    print(matches.groups())
    INGREDIENTS[matches.groups()[0]] = (
        int(matches.groups()[1]),
        int(matches.groups()[2]),
        int(matches.groups()[3]),
        int(matches.groups()[4]),
        int(matches.groups()[5]),
    )

print(INGREDIENTS)

TARGET_SIZE = 100
TARGET_CALORIES = 500  # For part 2
best_mix = -1


def solve(ingredients, total, mix, check_calories=False):
    global best_mix

    if not ingredients:
        if total == TARGET_SIZE:
            mix_totals = [0, 0, 0, 0]
            calories = 0
            for m, x in mix:
                for k in range(4):
                    mix_totals[k] += m[k] * x
                calories += m[4] * x
            if check_calories and calories != TARGET_CALORIES:
                return
            for i, v in enumerate(mix_totals):
                if v < 0:
                    mix_totals[i] = 0
            best_mix = max(best_mix, reduce(lambda a, b: a * b, mix_totals, 1))
    else:
        curr_ingredient = INGREDIENTS[ingredients[0]]
        for i in range(1, TARGET_SIZE):
            if i + total > TARGET_SIZE:
                # Too much
                continue
            else:
                new_mix = mix[:]
                new_mix.append((curr_ingredient, i))
                solve(ingredients[1:], total + i, new_mix, check_calories)


solve(list(INGREDIENTS.keys()), 0, [])

# 222870
print(f"answer = {best_mix}")

# Part 2
best_mix = -1
solve(list(INGREDIENTS.keys()), 0, [], check_calories=True)

# 117936
print(f"answer = {best_mix}")
