PUZZLE_INPUT = 36_000_000


# Highest scorers in sections of the houses are going to have the maximum number
# of factors, e.g. 2, 6, 24, 120
# These will be the step sizes, but starting from the biggest.
stepsizes = []

total = 1
for i in range(2, 10):
    total *= i
    stepsizes.insert(0, total)


house = stepsizes[0]
index = 0

best_so_far = 100000000000000000000000

for stepsize in stepsizes:
    print("start", house)
    while True:
        total = 0
        house += stepsize

        # Anything above house / 2 cannot be a factor
        for i in range(1, (house // 2) + 1):
            if house % i == 0:
                total += i * 10
        # Except the house itself
        total += house * 10
        if total >= PUZZLE_INPUT:
            if house < best_so_far:
                best_so_far = house
            # Go back two steps - WHY TWO?
            print(house)
            house -= 2 * stepsize
            # Move to the next (smaller) step-size
            break

# 831600
print(f"answer = {best_so_far}")

