PUZZLE_INPUT = 36_000_000


# Highest scorers in sections of the houses are going to have the maximum number
# of factors, e.g. 2, 6, 24, 120
# These will be the step sizes, but starting from the biggest.
stepsizes = []

total = 1
for i in range(2, 10):
    total *= i
    stepsizes.insert(0, total)


def calc_number(house):
    total = 0
    # Anything above house / 2 cannot be a factor
    for i in range(1, (house // 2) + 1):
        if house % i == 0:
            total += i * 10
    # Except the house itself
    total += house * 10
    return total


house = stepsizes[0]
best_so_far = 100000000000000000000000

for stepsize in stepsizes:
    while True:
        house += stepsize

        total = calc_number(house)
        if total >= PUZZLE_INPUT:
            if house < best_so_far:
                best_so_far = house
            # Go back two steps - WHY TWO?
            house -= 2 * stepsize
            # Move to the next (smaller) step-size
            break

# 831600
print(f"answer = {best_so_far}")

# Part 2
house = stepsizes[0]
best_so_far = 100000000000000000000000

for stepsize in stepsizes:
    while True:
        total = 0
        house += stepsize

        # Anything above house / 2 cannot be a factor
        for i in range(1, (house // 2) + 1):
            if house % i == 0 and i * 50 > house:
                total += i * 11
        # Except the house itself
        total += house * 11
        if total >= PUZZLE_INPUT:
            if house < best_so_far:
                best_so_far = house
            # Go back four steps - WHY FOUR?
            house -= 4 * stepsize
            if house < 0:
                house = 0
            # Move to the next (smaller) step-size
            break

# 884520
print(f"answer = {best_so_far}")

